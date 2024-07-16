document.addEventListener("DOMContentLoaded", () => {
    const preview_img = document.querySelector(".product_details .preview-img img")
    document.querySelectorAll(".product_details .img-list img").forEach(img => img.addEventListener("click", () => {
        preview_img.src = img.src;
        img.parentElement.querySelector(".active").classList.remove("active")
        img.classList.add("active")
    }))
})