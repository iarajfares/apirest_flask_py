const app = Vue.createApp({
    data() {
        return {
            productos: [],
            productoEditado: {
                idproductos: 0,
                nombre:'',
                descripcion: '',
                precio: 0
            }
        }
    },
    methods: {
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
        // EDITAR PRODUCTOS //
        async editarProducto(idproductos) {
            try {
                const id = this.productoEditado.idproductos
                const response = await fetch(`http://127.0.0.1:5000/productos/${idproductos}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.productoEditado)
                });
                if (response.ok) {
                    console.log('Producto editado con éxito.');
                    this.obtenerProductos();
                } else {
                    console.error('Error al editar el producto:', response.statusText);
                }
            } catch (error) {
                console.error('Error al editar el producto:', error);
            }
        },
        // ELIMINAR PRODUCTOS //
        eliminarProducto(idproductos) {
            fetch(`http://127.0.0.1:5000/productos/${idproductos}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    console.log('Producto eliminado con éxito.');
                    this.obtenerProductos();
                } else {
                    console.error('Error al eliminar el producto:', response.statusText);
                }
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
        },
        // NUEVO PRODUCTO // 
        async nuevoProducto() {
            try {
                const response = await fetch('http://127.0.0.1:5000/productos', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.nuevoProducto)
                });
                if (response.ok) {
                    console.log('Producto agregado con éxito.');
                    this.obtenerProductos();
                    this.nuevoProducto = {
                        nombre: '',
                        descripcion: '',
                        precio: 0,
                    };
                } else {
                    console.error('Error al agregar el producto:', response.statusText);
                }
            } catch (error) {
                console.error('Error al agregar el producto:', error);
            }
        }
    },
    mounted() {
        this.obtenerProductos(); 
    }
});

app.mount('#app');


