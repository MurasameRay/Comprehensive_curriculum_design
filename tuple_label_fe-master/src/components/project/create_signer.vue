<template>
  <Form
    :model="formItem2"
    :label-width="100"
  >
    <FormItem label="Signer Name">
      <Input
        v-model="formItem2.name"
        placeholder="Enter Signer Name"
      />
    </FormItem>
    <FormItem label="Signer UserName">
      <Input
        v-model="formItem2.username"
        placeholder="Enter Signer UserName"
      />
    </FormItem>
  </Form>
</template>
<script>
const axios = require("axios");
import urlSetting from "../../setting";

export default {
  data() {
    return {
      formItem2: {
        admin_id:"",
        name:"",
        username: ""
      }
    };
  },
  methods: {
    addSigner(callback) {
      this.formItem.admin_id=0;
      axios({
        method: "post",
        url: urlSetting.username_url,
        data: this.formItem2
      })
        .then(response => {
          if (response.status === 201) {
            console.log(response);
            this.$Message.success("创建成功");
          }
        })
        .catch(error => {
          this.$Message.error(error.data.message);
        })
        .then(() => {
          callback();
        });
    }
  }
};
</script>