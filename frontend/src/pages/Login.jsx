import React, {useState} from 'react'
import { Table, Button } from "react-bootstrap";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const performLogin = async ()=>{
        console.log(username,password);
        try{
            const res = await fetch("http://127.0.0.1:8000/ul/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                username,
                password
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
      <h3>Login Form</h3>
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
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
        <br />
        <Button
          className="form-control"
          variant="outline-success"
          onClick={performLogin}
        >
          Login
        </Button>
      </form>
    </div>
  );
}
