import React, { useState, useEffect } from 'react';
import { Table, Button} from 'react-bootstrap';
export default function Persons() {
  const [persons, setPersons] = useState([]);
  const [is_true, setIs_true] = useState(false)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [phone_number, setPhone_number] = useState('')
  const [date_of_birth, setDate_of_birth] = useState('')
  const [gender, setGender] = useState('')
  const [is_marride, setIs_marride] = useState('')
  const [address, setAddress] = useState('')
  const [p_id, setP_id] = useState()

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('http://localhost:8000/pl');
      const jsonData = await response.json();
      setPersons(jsonData);
    }
    fetchData();
  }, [persons]);

  let handleEdit = (person) =>{
    console.log('editButton Cliked',person);
    setP_id(person.id)
    setIs_true(true)
    setName(person.name)
    setEmail(person.email)
    setPhone_number(person.phone_number)
    setDate_of_birth(person.date_of_birth)
    setGender(person.gender)
    setIs_marride(person.is_marride)
    setAddress(person.address)
    
  }
  
  let handleDelete = async (id) => {
    try {
        const response = await fetch(`http://localhost:8000/pd/${id}/`, {
            method: 'DELETE',
        });

        if (!response.ok) {
            throw new Error('Failed to delete data');
        }

        // If the deletion is successful, you may want to update the UI or fetch updated data
        // const updatedPersons = persons.filter(person => person.id !== id);
        // setPersons(updatedPersons);

        console.log('Data deleted successfully');
    } catch (error) {
        console.error('Error deleting data:', error.message);
    }
  };

  let performUpdate = async (e) => {
    e.preventDefault();

    try {
        const response = await fetch(`http://localhost:8000/pu/${p_id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                email,
                phone_number,
                date_of_birth,
                gender,
                is_marride,
                address
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to submit data');
        }

        // If the submission is successful, you may want to clear the form fields or fetch updated data
        setName('');
        setEmail('');
        setPhone_number('');
        setDate_of_birth('');
        setGender('');
        setIs_marride('');
        setAddress('');
        setIs_true(false)

        // Fetch updated data
        // const fetchData = async () => {
        //     const response = await fetch('http://localhost:8000/pl');
        //     const jsonData = await response.json();
        //     setPersons(jsonData);
        // };
        // fetchData();

        console.log('Data submitted successfully');
    } catch (error) {
        console.error('Error submitting data:', error.message);
    }
  };

  let handleSubmit = async (e) => {
    e.preventDefault();

    try {
        const response = await fetch('http://localhost:8000/pc/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                email,
                phone_number,
                date_of_birth,
                gender,
                is_marride,
                address
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to submit data');
        }

        // If the submission is successful, you may want to clear the form fields or fetch updated data
        setName('');
        setEmail('');
        setPhone_number('');
        setDate_of_birth('');
        setGender('');
        setIs_marride('');
        setAddress('');

        // Fetch updated data
        // const fetchData = async () => {
        //     const response = await fetch('http://localhost:8000/pl');
        //     const jsonData = await response.json();
        //     setPersons(jsonData);
        // };
        // fetchData();

        console.log('Data submitted successfully');
    } catch (error) {
        console.error('Error submitting data:', error.message);
    }
  };

  console.log('hi');
  return (
    <>
    <div className="row">
      <div className="col col-2">
        <h5>Person Create/Update Form</h5>
        <form >
          <input className='form-control' type="text" placeholder='Enter Name' value={name} onChange={e=> setName(e.target.value)}/><br />
          <input className='form-control' type="text" placeholder='Email' value={email} onChange={e=> setEmail(e.target.value)}/><br />
          <input className='form-control' type="text" placeholder='Phone_number' value={phone_number} onChange={e=> setPhone_number(e.target.value)}/><br />
          <input className='form-control' type="date" placeholder='Date_of_birth' value={date_of_birth} onChange={e=> setDate_of_birth(e.target.value)}/><br />
     
          <select className='form-control' value={gender} onChange={e=> setGender(e.target.value)}>
            <option value="">Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Others">Others</option>
          </select>
          <br/>
          <label className='form-control'  htmlFor="">Is_marride: <input  type="checkbox" value={is_marride} onChange={e=> setIs_marride(e.target.value)}/></label>
          <br />
          <input className='form-control' type="text" placeholder='Address' value={address} onChange={e=> setAddress(e.target.value)}/><br />
          { is_true ? <Button className='form-control' variant="outline-info" onClick={performUpdate}>Update</Button> : <Button className='form-control' variant="outline-primary" onClick={handleSubmit}>Submit</Button>}
        </form>
      </div>
      <div className='col col-10'>
        <h1>Persons Information</h1>
        <Table striped bordered hover>
          <thead>
            <tr>
            <th>Photo</th>
              <th>Name</th>
              {/* <th>Email</th> */}
              <th>Phone_number</th>
              <th>Date_of_birth</th>
              <th>Gender</th>
              <th>Is_married</th>
              <th>Address</th>
              <th>Cars</th>
              <th>Action</th>
              
            </tr>
          </thead>
          <tbody>
            {persons.map(person => (
              <tr key={person.id}>
                <td><img src={person.photo} alt="" style={{ width: '30px', height: '30px', borderRadius:'100%' }} /></td>
                <td>{person.name}</td>
                {/* <td>{person.email}</td> */}
                <td>{person.phone_number}</td>
                <td>{person.date_of_birth}</td>
                <td>{person.gender}</td>
                <td>{person.is_married}</td>
                <td>{person.address}</td>
                <td><Button variant="outline-info" size='sm'>cars</Button></td>
                <td><Button variant="outline-info" size='sm' onClick={()=> handleEdit(person)}>Edit</Button>{' '}<Button variant="outline-danger" size='sm' onClick={()=> handleDelete(person.id)}>Delete</Button>{' '}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </div>
    </>
  );
}
