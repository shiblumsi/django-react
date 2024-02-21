import React, {useState} from 'react'

export default function Car() {
    const [cars, setCars] = useState([])
  return (
    <div>
        {/* <Table striped bordered hover>
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
                <td><Button variant="outline-info" size='sm' onClick={()=> handleEdit(person)}>Edit</Button>{' '}<Button variant="outline-danger" size='sm' onClick={()=> handleDelete(person.id)}>Delete</Button>{' '}</td>
              </tr>
            ))}
          </tbody>
        </Table> */}
    </div>
  )
}
