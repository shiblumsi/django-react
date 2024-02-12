
import React, { useState } from 'react'
import { Table, Button } from "react-bootstrap";

export default function Signup() {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('');

      
    const performRegister = async ()=>{
        console.log(username,email,password,password2);
        try{
            const res = await fetch("http://127.0.0.1:8000/ur/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                username,
                email,
                password,
                password2,
              }),
            });
            if (res.ok){
                console.log('data submitted');
            } else {
            console.error('Failed to send data');
            }
        }
        catch (error) {
            console.error('Error',error);
        }
        

        
    }
  return (
    <div>
        <h3>Signup Form</h3>
        <form>
            <input
            className="form-control"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Username"
            />
            <br />
            <input
            className="form-control"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            />
            <br />
            <input
            className="form-control"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            />
            <br />
            <input
            className="form-control"
            type="password"
            value={password2}
            onChange={(e) => setPassword2(e.target.value)}
            placeholder="Password 2"
            />
            <br />
            <Button className='form-control' variant="outline-success" onClick={performRegister}>Register</Button>
        </form>
    </div>
  );
}
