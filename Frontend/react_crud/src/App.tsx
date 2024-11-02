import './App.css';
import Products from "./admin/Components/Products";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./main/Main";
import ProductsCreate from "./admin/Components/ProductsCreate";
import ProductsEdit from "./admin/Components/ProductsEdit";
import User from "./User/User";

function App() {
    return (
    <>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<User />} />
                    <Route path="/home" element={<Main />} />
                    <Route path="/admin/products" element={<Products />} />
                    <Route path="/admin/products/create" element={<ProductsCreate />} />
                    <Route path="/admin/products/:id/edit" element={<ProductsEdit />} />    
                </Routes>
            </BrowserRouter>
    </>
    );
}

export default App;
