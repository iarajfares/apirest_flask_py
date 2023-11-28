// const url = 'http://127.0.0.1:5000/productos'
// DEFINIR VARIABLES //
const modalCrear = new bootstrap.Modal(document.getElementById('modalCrear'));
const formCrear = document.querySelector('#formCrear');
const nombreProducto = document.getElementById('nombre_producto');
const descripcionProducto = document.getElementById('descripcion_producto');
const precioProducto = document.getElementById('precio_producto');
let opcion = ''

btnCrear.addEventListener('click', ()=> {
    nombreProducto.value = ''
    descripcionProducto.value = ''
    precioProducto.value = ''
    modalCrear.show()
    opcion = 'Crear'
})