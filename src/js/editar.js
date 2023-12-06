console.log(location.search) 
var id = location.search.substr(4)
console.log(id)
const {
    createApp
} = Vue
createApp({
    data() {
        return {
            productos: [],
            idproductos: '',
            productos_name:"",
            productos_descripcion: "",
            productos_precio:'',
            imagen: "",

            //url:'http://127.0.0.1:5000/productos/' + id, //ruta local
            url: 'http://127.0.0.1:5000/productos/' + id,
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.idproductos = data.idproductos
                    this.productos_name  = data.productos_name
                    this.productos_descripcion = data.productos_descripcion
                    this.productos_precio = data.productos_precio
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        modificar() {
            let producto = {
                productos_name: this.productos_name,
                productos_descripcion: this.productos_descripcion,
                productos_precio: this.productos_precio
            }
            
            var options = {
                body: JSON.stringify(producto),
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                redirect: 'follow'
            }
            console.log('Datos a enviar:', JSON.stringify(producto));
            fetch(this.url, options)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(function(data) {
            console.log('Respuesta del servidor:', data);
            alert("Registro modificado");
            window.location.href = "./productos.html";
        })
        .catch(function(error) {
            console.error('Error en la solicitud:', error);
            alert("Error al Modificar");
        });
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')