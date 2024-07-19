document.addEventListener("DOMContentLoaded", () => {
    const preview_img = document.querySelector(".product_details .preview-img img")
    document.querySelectorAll(".product_details .img-list img").forEach(img => img.addEventListener("click", () => {
        preview_img.src = img.src;
        img.parentElement.querySelector(".active").classList.remove("active")
        img.classList.add("active")
    }))

    // listen for product remove from cart
    // show confirmation modal
    document.querySelectorAll(".trigger-modal-cta").forEach(cta => cta.addEventListener("click", () => {
        const link = cta.getAttribute("data-link")
        // close all open modals
        document.querySelectorAll(".modal.show").forEach(elem => elem.classList.remove("show"))
        // get modal and show on screen
        const modal = document.querySelector(".modal")
        // make link as form action
        modal.querySelector("form").action = link
        modal.classList.add("show")

    }))

    // cancel btn in modal should close modal and clear form action
    document.querySelector(".modal #cancel_cta").addEventListener("click", () => {
        const modal = document.querySelector(".modal")
        modal.querySelector("form").action = ""
        modal.classList.remove("show")

    })

    // user account toggle
    document.querySelector("#tab-dropdown-cta").addEventListener("click", () => {
        const dropdown = document.querySelector(".nav-drop")
        const cta_icon = document.querySelector("#tab-dropdown-cta i")
        if (dropdown.classList.contains("show")) {
            dropdown.classList.remove("show")
            cta_icon.classList.remove("fa-close")
            cta_icon.classList.add("fa-user")
        } else {
            dropdown.classList.add("show")
            cta_icon.classList.remove("fa-user")
            cta_icon.classList.add("fa-close")
        }
    })
})