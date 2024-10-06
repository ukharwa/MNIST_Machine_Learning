const inpCanvas = document.getElementById("input-canvas");
const outCanvas = document.getElementById("output-canvas");
const reset = document.getElementById("reset");
const submit = document.getElementById("submit");
let isDrawing = false;

class Canvas{
    constructor(dim, cssGrid){
        this.canvas = cssGrid;
        this.arrGrid = new Array(dim * dim).fill(0);
        this.dim = dim;
    }

    renderGrid = () => {
        if (!this.canvas.innerHTML){
            this.canvas.style.gridTemplate = `repeat(${this.dim}, 1fr) / repeat(${this.dim}, 1fr)`;
            let i = 0;
            const pixelHTML = this.arrGrid.map(() => {
                i++;
                return `<div class="pixel" id="pixel-${i}"></div>`
            }).join("");
            
            this.canvas.innerHTML = pixelHTML;
    
            this.arrPixels = Array.from(document.getElementsByClassName("pixel"));
        }
    
        for (let i of this.arrPixels){
            let color = this.arrGrid[this.arrPixels.indexOf(i)];
            i.style.backgroundColor = `rgb(${color}, ${color}, ${color})`;
        }
    
    }

    antiAlias = (pixelIndex) => {
        if (pixelIndex + this.dim - 1 < this.arrGrid.length){
            this.arrGrid[pixelIndex + this.dim - 1] += 32;
        }
        if (pixelIndex + this.dim < this.arrGrid.length){
            this.arrGrid[pixelIndex + this.dim] += 64;
        }
        if (pixelIndex + this.dim + 1 < this.arrGrid.length){
            this.arrGrid[pixelIndex + this.dim + 1] += 32;
        }
        if (pixelIndex - this.dim - 1 < this.arrGrid.length){
            this.arrGrid[pixelIndex - this.dim - 1] += 32;
        }
        if (pixelIndex - this.dim >= 0){
            this.arrGrid[pixelIndex - this.dim] += 64;
        }
        if (pixelIndex - this.dim + 1 >= 0){
            this.arrGrid[pixelIndex - this.dim + 1] += 32;
        }
    
        const row = Math.floor(pixelIndex / this.dim);
        if ((pixelIndex + 1) < this.arrGrid.length && Math.floor((pixelIndex + 1) / this.dim) === row) {
            this.arrGrid[pixelIndex + 1] += 64;
        }
        if ((pixelIndex - 1) >= 0 && Math.floor((pixelIndex - 1) / this.dim) === row) {
            this.arrGrid[pixelIndex - 1] += 64;
        }
    
        for (let i = 0; i < this.arrGrid.length; i++){
            if (this.arrGrid[i] > 255){
                this.arrGrid[i] = 255;
            }
        }
    }

    updatePixelDrag = (event) => {
        if (!isDrawing) return;
    
        const pixel = event.target;
        const pixelIndex = this.arrPixels.indexOf(pixel);
    
        this.arrGrid[pixelIndex] = 200;
        this.antiAlias(pixelIndex);
        this.renderGrid();
    }

    updatePixel = (event) => {
        const pixel = event.target;
        const pixelIndex = this.arrPixels.indexOf(pixel);
    
        this.arrGrid[pixelIndex] = 200;
        this.antiAlias(pixelIndex);
        this.renderGrid();
    }

    resetGrid = () => {
        for (let i = 0; i < this.arrGrid.length; i++) {
            this.arrGrid[i] = 0;
        }
    
        this.renderGrid();
    }
    
    reshape1Dto2D() {    
        const reshapedArray = [];
        for (let i = 0; i < this.dim; i++) {
            reshapedArray.push(this.arrGrid.slice(i * this.dim, i * this.dim + this.dim));
        }
        return reshapedArray;
    }

    downsampleGrid(lowResDim) {
        const highResGrid = this.reshape1Dto2D(this.arrGrid);
        const blockSize = this.dim / lowResDim;   // 560 / 28 = 20
    
        const lowResGrid = new Array(lowResDim).fill(0).map(() => new Array(lowResDim).fill(0));
    
        for (let y = 0; y < lowResDim; y++) {
            for (let x = 0; x < lowResDim; x++) {
                let sum = 0;
                let count = 0;
    
                // Sum the pixels in the corresponding block from the highResGrid
                for (let i = 0; i < blockSize; i++) {
                    for (let j = 0; j < blockSize; j++) {
                        const highResX = x * blockSize + j;
                        const highResY = y * blockSize + i;
                        
                        sum += highResGrid[highResY][highResX];
                        count++;
                    }
                }
    
                // Calculate the average value for the low-res pixel
                lowResGrid[y][x] = sum / count;
            }
        }
    
        return lowResGrid;
    }

    initialize = () => {
        this.renderGrid();
        for (let i of this.arrPixels) {
            i.addEventListener("mouseover", this.updatePixelDrag);
            i.addEventListener("mouseenter", this.updatePixelDrag);
            i.addEventListener("mouseout", this.updatePixelDrag);
            i.addEventListener("click", this.updatePixel);
        }
    }

}

const handleMouseDown = () => {
    isDrawing = true;
};

const handleMouseUp = () => {
    isDrawing = false;
};

const renderOutGrid = (array) => {
    const pixelHTML = array.map(() => {
        return `<div class="out-pixel"></div>`
    }).join("");
    
    outCanvas.innerHTML = pixelHTML;

    const arrOutPixels = Array.from(document.getElementsByClassName("out-pixel"));

    for (let i of arrOutPixels){
        color = array[arrOutPixels.indexOf(i)];
        i.style.backgroundColor = `rgb(${color}, ${color}, ${color})`;
    }
}

const initializeListeners = () => {
    const canvas = new Canvas(56, inpCanvas);
    canvas.initialize();
    inpCanvas.addEventListener("mousedown", handleMouseDown);
    inpCanvas.addEventListener("mouseup", handleMouseUp);
    
    const output = () => {
        const outputGrid = canvas.downsampleGrid(28).flat();
        renderOutGrid(outputGrid);
        console.log(outputGrid.join(","))
    }

    submit.addEventListener("click", output)
    reset.addEventListener("click", canvas.resetGrid);

};

initializeListeners();
