let covers = document.getElementsByClassName("book-cover")

for (let cover of covers) {
    cover.addEventListener("load", event => {
        cover.setAttribute("style", "filter: blur(0px);")
        console.log("Image loaded")
    })
    cover.addEventListener("mouseover", event => {
        cover.setAttribute("style", "filter: blur(0px);")
    });
}