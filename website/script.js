const canvas = document.getElementById("input-canvas");
const outCanvas = document.getElementById("output-canvas");
const reset = document.getElementById("reset");
const submit = document.getElementById("submit");
let arrPixels;
let isDrawing = false;

const arrGrid = new Array(7056).fill(0);


const renderGrid = (array) => {
    if (!canvas.innerHTML){
        let i = 0;
        const pixelHTML = array.map(() => {
            i++;
            return `<div class="pixel" id="pixel-${i}"></div>`
        }).join("");
        
        canvas.innerHTML = pixelHTML;

        arrPixels = Array.from(document.getElementsByClassName("pixel"));
    }

    for (let i of arrPixels){
        color = array[arrPixels.indexOf(i)];
        i.style.backgroundColor = `rgb(${color}, ${color}, ${color})`;
    }

}
renderGrid(arrGrid);

const antiAlias = (pixelIndex ,rowLength) => {
    if (pixelIndex + rowLength - 1 < arrGrid.length){
        arrGrid[pixelIndex + rowLength - 1] += 32;
    }
    if (pixelIndex + rowLength < arrGrid.length){
        arrGrid[pixelIndex + rowLength] += 64;
    }
    if (pixelIndex + rowLength + 1 < arrGrid.length){
        arrGrid[pixelIndex + rowLength + 1] += 32;
    }
    if (pixelIndex - rowLength - 1 < arrGrid.length){
        arrGrid[pixelIndex - rowLength - 1] += 32;
    }
    if (pixelIndex - rowLength >= 0){
        arrGrid[pixelIndex - rowLength] += 64;
    }
    if (pixelIndex - rowLength + 1 >= 0){
        arrGrid[pixelIndex - rowLength + 1] += 32;
    }

    const row = Math.floor(pixelIndex / rowLength);
    if ((pixelIndex + 1) < arrGrid.length && Math.floor((pixelIndex + 1) / rowLength) === row) {
        arrGrid[pixelIndex + 1] += 64;
    }
    if ((pixelIndex - 1) >= 0 && Math.floor((pixelIndex - 1) / rowLength) === row) {
        arrGrid[pixelIndex - 1] += 64;
    }

    for (let i = 0; i < arrGrid.length; i++){
        if (arrGrid[i] > 255){
            arrGrid[i] = 255;
        }
    }
}

const updatePixelDrag = (event) => {
    if (!isDrawing) return;

    const pixel = event.target;
    const pixelIndex = arrPixels.indexOf(pixel);
    const rowLength = Math.sqrt(arrGrid.length);

    arrGrid[pixelIndex] = 255;
    antiAlias(pixelIndex, rowLength);
    renderGrid(arrGrid);
};

const updatePixel = (event) => {

    const pixel = event.target;
    const pixelIndex = arrPixels.indexOf(pixel);
    const rowLength = Math.sqrt(arrGrid.length);

    arrGrid[pixelIndex] = 255;
    antiAlias(pixelIndex, rowLength);
    renderGrid(arrGrid);
};

const resetGrid = () => {
    for (let i = 0; i < arrGrid.length; i++) {
        arrGrid[i] = 0;
    }

    renderGrid(arrGrid);
};

const handleMouseDown = () => {
    isDrawing = true;
};

const handleMouseUp = () => {
    isDrawing = false;
};

function reshape1Dto2D(arr) {
    const dim = Math.sqrt(arr.length)

    const reshapedArray = [];
    for (let i = 0; i < dim; i++) {
        reshapedArray.push(arr.slice(i * dim, i * dim + dim));
    }
    return reshapedArray;
}


function downsampleGrid(highResGrid, lowResDim) {
    const blockSize = highResGrid[0].length / lowResDim;   // 560 / 28 = 20

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

const output = () => {
    const outputGrid = downsampleGrid(reshape1Dto2D(arrGrid), 28).flat();
    renderOutGrid(outputGrid);
    console.log(outputGrid.join(","))
}

const initializeListeners = () => {
    for (let i of arrPixels) {
        i.addEventListener("mouseover", updatePixelDrag);
        i.addEventListener("mouseenter", updatePixelDrag);
        i.addEventListener("mouseout", updatePixelDrag);
        i.addEventListener("click", updatePixel);
    }
    canvas.addEventListener("mousedown", handleMouseDown);
    canvas.addEventListener("mouseup", handleMouseUp);

    submit.addEventListener("click", output)
    reset.addEventListener("click", resetGrid);
};

initializeListeners();
