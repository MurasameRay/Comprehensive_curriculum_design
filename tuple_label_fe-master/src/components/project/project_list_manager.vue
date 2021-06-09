<template>
  <div>
    <div>
      <Row>
        <Col span="1">
        <Button
          @click="createProjectOption.isShow = true"
          type="success"
        >新增项目</Button>
        </Col>
      </Row>

      <Table
        highlight-row
        :columns="columns1"
        :data="data1"
      ></Table>

      <Modal
        v-model="showEditModal"
        title="编辑项目"
        @on-ok="ok"
        @on-cancel="cancel"
      >
        <Form
          :model="editData"
          :label-width="80"
        >
          <FormItem label="ID">
            <Input
              disabled
              v-model="editData.id"
            />
          </FormItem>
          <FormItem label="Project Name">
            <Input v-model="editData.name" />
          </FormItem>
          <FormItem label="Description">
            <Input v-model="editData.description" />
          </FormItem>
        </Form>
      </Modal>

      <Modal
        v-model="createProjectOption.isShow"
        title="新建项目"
        @on-ok="createProjectOk"
        @on-cancel="createProjectOption.isShow = false"
      >
        <CreateProject ref="CreateProject"></CreateProject>
      </Modal>
    </div>
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
      :columns="columns2"
      :data="data2"
    ></Table>

      <Modal
        v-model="showEditModal2"
        title="管理用户"
      >
        <Form
          :model="editData2"
          :label-width="80"
        >
          <FormItem label="id">
            <Input
              disabled
              v-model="editData2.id"
            />
          </FormItem>
          <FormItem label="name">
            <Input v-model="editData2.name" />
          </FormItem>
          <FormItem label="user_name">
            <Input v-model="editData2.username" />
          </FormItem>
        </Form>
      </Modal>
<div class="ant-modal-header" ref="refModel">
      <Modal
        v-model="createSignerOption.isShow"
        title="新增标注员"
        @on-ok="createSignerOk"
        @on-cancel="createSigner_cancel"
        :getContainer="() => $refs.refModel"
      >
      
        <CreateSigner ref="CreateSigner"></CreateSigner>
      </Modal>
      </div>
    </div>
  </div>
</template>
<script>
	
const axios = require("axios");
import urlSetting from "../../setting";
import CreateProject from "./create_project";
import CreateSigner from "./create_signer";

export default {
  data() {
    return {
      showEditModal: false,
      columns1: [
        {
          title: "ID",
          key: "id"
        },
        {
          title: "Project Name",
          key: "name"
        },
        {
          title: "Description",
          key: "description"
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
                    size: "default",
                    to: `/project/${params.row.id}/documents`
                  },
                  style: {
                    marginRight: "5px"
                  }
                },
                "详情"
              ),
              h(
                "Button",
                {
                  props: {
                    type: "primary",
                    size: "default"
                  },
                  on: {
                    click: () => {
                      this.editProject(params.row);
                    }
                  }
                },
                "编辑"
              ),
              h(
                "Button",
                {
                  props: {
                    type: "error",
                    size: "default"
                  },
                  on: {
                    click: () => {
                      this.doDelete(params.row);
                    }
                  }
                },
                "删除"
              ),
			  h(
			    "Button",
			    {
			      props: {
			        type: "success",
			        size: "default",
			        to: `/management/manage`
			      },
			    },
			    "管理"
			  ),
            ]);
          }
        }
      ],
      columns2: [
        {
          title: "User_ID",
          key: "id"
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
                    type: "error",
                    size: "default"
                  },
                  on: {
                    click: () => {
                      this.doDelete_Signer(params.row);
                    }
                  }
                },
                "删除"
              ),
            ]);
          }
        }
      ],
      data1: [],
      editData: {
        id: "",
        name: "",
        description: "",
        admin_id:""
      },
      data2: [],
      editData2: {
        id: "",
        name: "",
        username: ""
      },
      createProjectOption: {
        isShow: false
      },
      createSignerOption:{
        isShow:false
      }
    };
  },
  mounted() {
    this.search_adminID();    "通过注册获得的username和admin表匹配获取admin的ID"
    this.search_admin();      "通过获取的adminID将signer里面相同ID的记录输出"
    this.search_project();
  },
  methods: {
    search_project() {
      axios
        .get(`${urlSetting.project_url}?admin_id=${localStorage.getItem('admin_id')}`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
           this.data1=response.data.results;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },

    
    search_adminID() {
      axios
        .get(`${urlSetting.admin_url}?username=${localStorage.getItem('username')}`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            localStorage.setItem('admin_id', response.data.results[0].id);
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
    search_admin() {
      axios
        .get(`${urlSetting.username_url}?admin_id=${localStorage.getItem('admin_id')}`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.data2 = response.data.results;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        });
    },
  
	
    editProject(row) {
      axios
        .get(urlSetting.project_url + row.id + "/")
        .then(response => {
          if (response.status === 200) {
            this.editData = response.data;
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        })
        .then(() => {});

      this.showEditModal = true;
    },
	// 测试获取是否为管理员
	
	
    deleteProject(row) {
      axios
        .delete(urlSetting.project_url + row.id + "/")
        .then(response => {
          console.log(response);
          if (response.status === 204) {
            this.$Message.success("删除成功");
            this.search_project();
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        })
        .then(() => {});
    },
    doDelete(row) {
      this.$Modal.confirm({
        content: `确认删除 ${row.name} ？`,
        onOk: this.deleteProject.bind(null, row)
      });
    },
    doDelete_Signer(row) {
      this.$Modal.confirm({
        content: `确认删除 ${row.name} ？`,
        onOk: this.deleteSigner.bind(null, row)
      });
    },
    deleteSigner(row) {
      //login删除的是标注员
      // async valid => {
      // const response = await this.$http.put('/login/',row.username).catch(() => this.$message.error("删除失败,请联系Tel:"))
      // }
      row.admin_id="0";
      axios
        .put(urlSetting.username_url + row.id + "/", row)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.$Message.success("删除成功");
            this.search_admin();
            this.$refs.CreateSigner.search_admin();
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        })
        .then(() => {});
    },
    ok() {
      this.saveProject();
    },
    saveProject() {
      axios
        .put(urlSetting.project_url + this.editData.id + "/", this.editData)
        .then(response => {
          if (response.status === 200) {
            this.$Message.info("保存成功");
            this.search_project();
          }
        })
        .catch(error => {
          this.$Message.error(error.toString());
        })
        .then(() => {});
    },
    saveSigner() {
      axios
        .put(urlSetting.username_url + this.editData2.id + "/", this.editData2)
        .then(response => {
          if (response.status === 200) {
            this.$Message.info("保存成功");
            this.search_admin();
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
    createProjectOk() {
      this.$refs.CreateProject.addProject(this.search_project);
    },
    createSignerOk(){
      this.search_admin();
      this.$refs.CreateSigner.search_admin();
    },
    createSigner_cancel(){
      this.createSignerOption.isShow = false;
      this.search_admin();
      this.$refs.CreateSigner.search_admin();
    }
  },
  components: {
    CreateProject,
    CreateSigner
  },
};
</script>
