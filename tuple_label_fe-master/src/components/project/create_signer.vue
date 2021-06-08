<template>
  <div style="width:1000px">
    <div>
      <br><br>
      <Row>
        <Col span="1">
        <Button
          @click="createSignerOption.isShow = true"
          type="success"
        >添加标注员</Button>
        </Col>
      </Row>

      <Table
      highlight-row
      :columns="columns"
      :data="data"
    ></Table>

      <Modal
        v-model="showEditModal"
        title="管理用户"
        @on-ok="saveSignerOK"
        @on-cancel="cancel"
      >
        <Form
          :model="editData"
          :label-width="80"
          
        >
          <FormItem label="id">
            <Input
              disabled
              v-model="editData.id"
            />
          </FormItem>
          <FormItem label="name">
            <Input v-model="editData.name" />
          </FormItem>
          <FormItem label="user_name">
            <Input v-model="editData.username" />
          </FormItem>
        </Form>
      </Modal>

      <Modal
        v-model="createSignerOption.isShow"
        title="新增标注员"
        @on-ok="createSignerOk"
        @on-cancel="createSignerOption.isShow = false"
      >
        <CreateSigner ref="CreateSigner"></CreateSigner>
      </Modal>
    </div>
  </div>
</template>
<script>
const axios = require("axios");
import urlSetting from "../../setting";

export default {
  data() {
    return {
        columns: [
        {
          title: "User_ID",
          key: "id",
          width: "100px"
        },
        {
          title: "Name",
          key: "name"
        },
        {
          title: "User_Name",
          key: "username"
        },
        {
          title: "操作",
          key: "action",
          width: 400,
          align: "center",
          // 编辑和删除按钮
          render: (h, params) => {
            return h("div", [
              h(
                "Button",
                {
                  props: {
                    type: "primary",
                    size: "default"
                  },
                  on: {
                    click: () => {
                      this.addSigner(params.row);
                    }
                  }
                },
                "添加"
              ),
            ]);
          }
        }
      ],
      data: [],
      editData: {
        id: "",
        name: "",
        username: ""
      },
      createSignerOption:{
        isShow:false
      }
    };
  },
  mounted(){
    this.search_admin();
  },
  methods: {
    addSigner(callback) {
      axios
        .put(urlSetting.username_url + this.editData.id + "/", this.editData)
        .then(response => {
          if (response.status === 200) {
            this.$Message.info("保存成功");
            this.search();
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        })
        .then(() => {});
    },
    cancel() {
      this.$Message.info("取消编辑");
    },
    search_admin() {
      axios
        .get(`${urlSetting.username_url}?admin_id=0`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.data = response.data.results;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
  }
};
</script>