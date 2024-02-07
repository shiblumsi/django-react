import React, { useState, useEffect } from 'react';
import { Table, Button} from 'react-bootstrap';
export default function Persons() {
  const [persons, setPersons] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('http://localhost:8000/pl');
      const jsonData = await response.json();
      setPersons(jsonData);
    }
    fetchData();
  }, []);

  console.log(persons);
  
  return (
    <>
    <div className="row">
      <div className="col col-4">
        <h5>Person Create/Update Form</h5>
        <form action="">
          <input className='form-control' type="text" placeholder='Enter Name' /><br />
          <input className='form-control' type="text" placeholder='Email' /><br/>
          <input className='form-control' type="text" placeholder='Phone_number' /><br/>
          <input className='form-control' type="text" placeholder='Date_of_birth' /><br/>
     
          <select>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Others">Others</option>
          </select>
          <br/>
          <label htmlFor="">Is_marride:</label>
          <input  type="checkbox" /><br/>
          <input className='form-control' type="text" placeholder='Address' /><br/>
          <Button className='form-control' variant="outline-primary" >Submit</Button>
        </form>
      </div>
      <div className='col col-8'>
        <h1>Persons Information</h1>
        <Table striped bordered hover>
          <thead>
            <tr>
            <th>Photo</th>
              <th>Name</th>
              <th>Email</th>
              <th>Phone_number</th>
              <th>Date_of_birth</th>
              <th>Gender</th>
              <th>Is_married</th>
              <th>Address</th>
              <th>Action</th>
              
            </tr>
          </thead>
          <tbody>
            {persons.map(person => (
              <tr key={person.id}>
                <td><img src={person.photo} alt="" style={{ width: '30px', height: '30px', borderRadius:'100%' }} /></td>
                <td>{person.name}</td>
                <td>{person.email}</td>
                <td>{person.phone_number}</td>
                <td>{person.date_of_birth}</td>
                <td>{person.gender}</td>
                <td>{person.is_married}</td>
                <td>{person.address}</td>
                <td><Button variant="outline-info" size='sm'>Edit</Button>{' '}<Button variant="outline-danger" size='sm'>Delete</Button>{' '}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
    </>
  );
}
