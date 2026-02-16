import React, { useState, useEffect } from 'react';

const ProductDashboard = () => {
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [sortOrder, setSortOrder] = useState("low-to-high");

  const products = [
    {
      id: 1,
      name: "Wireless Headphones",
      price: 99.99,
      category: "Electronics",
      image_url: "https://via.placeholder.com/150"
    },
    {
      id: 2,
      name: "Cotton T-Shirt",
      price: 19.99,
      category: "Clothing",
      image_url: "https://via.placeholder.com/150"
    },
    {
      id: 3,
      name: "Stainless Steel Water Bottle",
      price: 24.99,
      category: "Accessories",
      image_url: "https://via.placeholder.com/150"
    },
    {
      id: 4,
      name: "Smart Watch",
      price: 199.99,
      category: "Electronics",
      image_url: "https://via.placeholder.com/150"
    },
    {
      id: 5,
      name: "Leather Wallet",
      price: 39.99,
      category: "Accessories",
      image_url: "https://via.placeholder.com/150"
    }
  ];

  useEffect(() => {
    let result = [...products];
    if (selectedCategory !== "All") {
      result = result.filter(product => product.category === selectedCategory);
    }
    result.sort((a, b) => sortOrder === "low-to-high" ? a.price - b.price : b.price - a.price);
    setFilteredProducts(result);
  }, [selectedCategory, sortOrder]);

  const handleSort = () => {
    setSortOrder(prevOrder => prevOrder === "low-to-high" ? "high-to-low" : "low-to-high");
  };

  const categories = ["All", ...new Set(products.map(product => product.category))];

  return (
    <div style={{ padding: '20px' }}>
      <div style={{ marginBottom: '20px' }}>
        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          style={{ padding: '8px', marginRight: '10px' }}
        >
          {categories.map(category => (
            <option key={category} value={category}>{category}</option>
          ))}
        </select>
        <button onClick={handleSort} style={{ padding: '8px 16px' }}>
          Sort: {sortOrder === "low-to-high" ? "Low to High" : "High to Low"}
        </button>
      </div>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
        gap: '20px'
      }}>
        {filteredProducts.map(product => (
          <div key={product.id} style={{
            border: '1px solid #ddd',
            padding: '15px',
            borderRadius: '5px',
            textAlign: 'center'
          }}>
            <img src={product.image_url} alt={product.name} style={{ width: '100%', height: '150px', objectFit: 'cover' }} />
            <h3>{product.name}</h3>
            <p>${product.price.toFixed(2)}</p>
            <p>{product.category}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductDashboard;