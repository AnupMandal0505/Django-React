import React from 'react'

const Data = ({users}) => {
  return (
   
       <>
          {
              users.map((curUser) => {
                  const {user_id, first_name,last_name,phone,email,age, user_type} = curUser;
                //   const {street, city, zipcode} = curUser.address;

                  return (
                      <tr key={user_id}>
                          <td>{user_id}</td>
                          <td>{first_name} {last_name}</td>
                          <td>{phone}</td>
                          <td>{email}</td>
                          <td>{age}</td>


                          {/* <td>{street}, {city}, {" "}, {zipcode}</td> */}
                      </tr>
                  )
              })

          }
      </>
   
  )
}

export default Data

// const UserData = ({users}) => {
//   return (
//       <>
//           {
//               users.map((curUser) => {
//                   const {id, name, email} = curUser;
//                   const {street, city, zipcode} = curUser.address;

//                   return (
//                       <tr key={id}>
//                           <td>{id}</td>
//                           <td>{name}</td>
//                           <td>{email}</td>
//                           <td>{street}, {city}, {" "}, {zipcode}</td>
//                       </tr>
//                   )
//               })

//           }
//       </>
//   )
// }
// export default UserData;