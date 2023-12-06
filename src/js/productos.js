const app = Vue.createApp({
    data() {
        return {
            productos: [],
            url: 'http://127.0.0.1:5000/productos',
                idproductos: '',
                productos_name:"",
                productos_descripcion: "",
                productos_precio:'',
                imagen: ""
        }
    },
    methods: {
        // CREAR PRODUCTOS //
        registrarProducto() {
            const formData = new FormData();
            formData.append('idproductos', this.idproductos);
            formData.append('productos_name', this.productos_name);
            formData.append('productos_descripcion', this.productos_descripcion);
            formData.append('productos_precio', this.productos_precio);
            fetch('http://127.0.0.1:5000/productos', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
            })
            .catch(error => {
                console.log('Error', error);
            })
        },
        // MOSTRAR PRODUCTOS //
        async obtenerProductos() {
            try {
                const response = await fetch('http://127.0.0.1:5000/productos');
                const data = await response.json();
                this.productos = data.Productos;
            } catch (error) {
                console.error('Error al obtener los productos:', error);
            }
        },
        // // EDITAR PRODUCTOS //
        redirigir(id) {
            // Redirige a la página de edición con el ID como parámetro
            window.location.href = 'editar.html?id=' + id;
        },   
        // // ELIMINAR PRODUCTOS //
        eliminarProducto(producto) {
            const idproductos = producto.idproductos;
            console.log('ID del producto a eliminar:', idproductos);
            alertify.confirm("Confirmar", "¿Estás seguro de que quieres eliminar este producto?",
            () => {
                fetch(`http://127.0.0.1:5000/productos/${idproductos}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    console.log('Producto eliminado con éxito.');
                    alertify.success('Producto eliminado con éxito.'); 
                    this.obtenerProductos();
                } else {
                    console.error('Error al eliminar el producto:', response.statusText);
                }
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
            },
            () => {
                alertify.error("Cancelado");
            });
        },
    },
    mounted() {
        this.obtenerProductos(); 
    }
});
app.mount('#app');



