import { useEffect, useState } from "react";
import './User.css'

export default function User() {
    const [isSignin, setIsSignin] = useState(false);

    const handleSignin = () => {
        if (isSignin === false){
            setIsSignin(true);
        }else{
        setIsSignin(false);
        }
    };

    return (
        <div className="form-container">
            <div className="form-box">
                <h4><b>Welcome</b></h4>
                <p>
                    Please {isSignin ? "sign in" : "sign up"} to continue.
                    <span onClick={handleSignin}> {isSignin ? "New in MiniWord?" : "Already our member"} </span>
                </p>
                <div className="box">
                    <form action="">
                        <label htmlFor="username">Username:</label>
                        <input type="text" id="username" placeholder="Enter your username"/>
    
                        {/* Conditionally render the email field if it's a sign-up form */}
                        {!isSignin && (
                            <>
                                <label htmlFor="email">Email:</label>
                                <input type="email" id="email" placeholder="Enter your email"/>
                            </>
                        )}
                        
                        <label htmlFor="password">Password:</label>
                        <input type="password" id="password" placeholder="Enter your password"/>
                        
                        <button type="submit">{isSignin ? "Sign In" : "Sign Up"}</button>
                    </form>
                </div>
            </div>
        </div>
    );
    
}
