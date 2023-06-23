import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
 

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };


  const handleSubmit = async (event) => {
    event.preventDefault();

    if (selectedFile) {
      const formData = new FormData();
      formData.append('image', selectedFile);
      formData.append("id_user","bf63fa6d-1199-11ee-a1b6-04421a2606de");
   
    

      try {
        await axios.post('http://localhost:8000/upload-avatar', formData);
        console.log('Ảnh đã được tải lên và hiển thị trước thành công');
      } catch (error) {
        console.error('Đã xảy ra lỗi:', error);
        
      }
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Tải lên</button>
      </form>
    </div>
  );
}

export default App;
