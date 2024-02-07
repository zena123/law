<template>
  <form @submit.prevent="submitRequest">
    <label for="clientName">Name:</label>
    <input v-model="client_name" type="text" required>

    <label for="clientEmail">Email:</label>
    <input v-model="client_email" type="email" required>

    <label for="clientPhone">Phone:</label>
    <input v-model="client_phone" type="tel" required>

    <label for="caseDescription">Case Description:</label>
    <textarea v-model="case_description" required></textarea>

    <label for="caseType">Case Type:</label>
    <input v-model="case_type" type="text" required>

    <label for="document">Document Attachment:</label>
    <input type="file" @change="handleFileChange" accept=".pdf">

    <button type="submit">Submit Request</button>
  </form>
</template>

<script>
import axios from 'axios';


export default {
  data() {
    return {
      client_name: '',
      client_email: '',
      client_phone: '',
      case_description: '',
      case_type: '',
      document: null,
    };
  },
  methods: {
    handleFileChange(event) {
      // Access the selected file
      this.document = event.target.files[0];
    },
    submitRequest() {
      // Validate form inputs and handle the submission
      if (this.validateForm()) {
        // Create a FormData object to handle file uploads
        const formData = new FormData();
        formData.append('client_name', this.client_name);
        formData.append('client_email', this.client_email);
        formData.append('client_phone', this.client_phone);
        formData.append('case_description', this.case_description);
        formData.append('case_type', this.case_type);
        formData.append('document', this.document);

        axios.post('/api/v1/legal-requests/', formData,
          { headers: { 'Content-Type': 'multipart/form-data' }}).then( response =>{
              console.log(response.data())
        }
        ).catch(
            console.log("error")

        )
          } else {
        console.log("unexpected error")
      }
      },
      validateForm() {
      // Implement form validation logic
      // Return true if the form is valid, otherwise false
    },
    },
};
</script>
