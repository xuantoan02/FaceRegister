
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Register from "./Register";
import Login from "./Login"
import UploadAvatar from "./component/UploadAvt"
import Admin from "./component/Admin"
import ProtectedRoute from "./component/ProtectedRoute"
import HomePage from "./component/HomePage"


// const App = () => {
//   return (
//     <Router>

//       <Routes>
//         <Route exact path="/" element={<HomePage />} />
//         <Route path="/Login" element={<Login/>} />
//         <Route path="/Register" element={<Register/>} />
//         <ProtectedRoute path="/Upload-avt" element={<UploadAvatar/>} />
//         <ProtectedRoute path="/Admin" element={<Admin/>} />
//       </Routes>
//     </Router>
//   );
// };

// export default App;



export default function App() {
  return (
    <Router>
      
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Register" element={<Register />} />
        <Route path="/Admin" element={<ProtectedRoute element={<Admin />} />} />
        {/* <ProtectedRoute path="/Upload-avt" component={UploadAvatar} />*/}
        {/* <Route path="/Admin" element={< ProtectedRoute element={<Admin/>} />} /> */}
      </Routes>
    </Router>
  );
}