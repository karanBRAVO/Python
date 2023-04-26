const showBigImgLayer = document.getElementById("showBigImgLayer");
const zoomImg = document.getElementById("zoomImg");
const mainImg = document.getElementById("mainImg");

mainImg.addEventListener('click', () => {
    showBigImgLayer.style.display = "flex";
    zoomImg.src = mainImg.src;
    alert("To close this window click on the image.");
});

zoomImg.addEventListener('click', ()=> {
    showBigImgLayer.style.display = "none";
    zoomImg.src = "";
});
