import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [error, setError] = useState(null);
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [quantity, setQuantity] = useState(1); 

  const fetchAPI = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5050/Products");
      setProducts(response.data);
    } catch (err) {
      console.error("Error fetching products: ", err);
      setError("Failed to fetch products");
    }
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  const addToCart = async (productId) => {
    try {
      const response = await axios.post("http://127.0.0.1:5050/Carts", {
        id_product: productId,
        quantity: quantity
      });
      console.log(response.data);
      setCart([...cart, { id_product: productId, quantity }]);
    } catch (err) {
      console.error("Error agregando productos al carrito: ", err);
      setError("Failed al agregar un producto al carrito");
    }
  };

  return (
    <div className="App">
      {error && <div className="error">{error}</div>}
      <h1>Todos los productos </h1>
      <ul className="product-list">
        {products.map(product => (
          <li key={product.id_product} className="product-item">
            <span className="product-name">{product.name}</span> 
            <span className="product-quantity">Cantidad: {product.quantity}</span>
            <input
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(Number(e.target.value))}
              min="1"
              className="quantity-input"
            />
            <button className="add-button" onClick={() => addToCart(product.id_product)}>Agregar</button>
          </li>
        ))}
      </ul>
      <h2>Carrito</h2>
      <ul className="cart-list">
        {cart.map((item, index) => (
          <li key={index} className="cart-item">
            Producto ID: {item.id_product} - Cantidad: {item.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
  
}

export default App;
