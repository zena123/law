<template>
  <div>
    <h2>Legal Requests Dashboard</h2>
    <table>
      <thead>
        <tr>
          <th>Client Name</th>
          <th>Case Type</th>
          <th>Submission Date</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="request in legalRequests" :key="request.id">
          <td>{{ request.client.name }}</td>
          <td>{{ request.case_type }}</td>
          <td>{{ request.submission_date }}</td>
          <td>
            <select v-model="request.status" @change="updateStatus(request)">
              <option value="open">Open</option>
              <option value="in_progress">In Progress</option>
              <option value="completed">Completed</option>
              <option value="rejected">Rejected</option>
            </select>
          </td>
          <td>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      legalRequests: [],
    };
  },
  created() {
    this.fetchLegalRequests();
  },
  methods: {
    fetchLegalRequests() {
      axios.get('api/v1/core/legal-requests/').then(results =>{
          this.legalRequests = results.data
      })

    },
    updateStatus(legalRequest) {
      axios.patch(`/api/v1/legal-requests/${legalRequest.id}/`, { status: legalRequest.status })
    },
  },
};
</script>
