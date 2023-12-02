document.getElementById("header").innerHTML= `
<nav class="navbar navbar-expand-sm navbar-light" style="background-color: #75B798"> 
<div class="container">
    <a class="navbar-brand" href="https://iarajfares.github.io/electrofive-cac/">Electro5</a>
    <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavId" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="acollapsibleNavId">
        <ul class="navbar-nav me-auto mt-2 mt-lg-0">
            <li class="nav-item">
                <a class="nav-link active" href="https://iarajfares.github.io/electrofive-cac/" aria-current="page" style="font-size: larger;">Home <span class="visually-hidden">(current)</span></a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-item dropdown-toggle" href="#" id="dropdownId" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: larger;">CRUD</a>
                <div class="dropdown-menu" aria-labelledby="dropdownId" style="background-color: #D1E7DD">
                    <a class="dropdown-item" href="../templates/productos.html">Productos</a>
                    <a class="dropdown-item" href="#">Action 2</a>
                </div>
            </li>
        </ul>
        <form class="d-flex my-2 my-lg-0">
            <input class="form-control me-sm-2" type="text" placeholder="Buscar">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Buscar</button>
        </form>
    </div>
</div>
</nav>
`