<template>
  <div>
    <Row>
      <Col span="1">

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

    
  </div>

</template>
<script>
	
const axios = require("axios");
import urlSetting from "../../setting";
import CreateProject from "./create_project";


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
                    type: "success",
                    size: "default",
                    to: `/annotation/${params.row.id}`
                  }
                },
                "开始标注"
              )
            ]);
          }
        }
      ],
      data1: [],
      editData: {
        id: "",
        name: "",
        description: "",
      },
      createProjectOption: {
        isShow: false
      }
    };
  },
  mounted() {
    this.search_user();
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
	  search_user() {
      axios
        .get(`${urlSetting.username_url}?username=${localStorage.getItem('username')}`)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            localStorage.setItem("admin_id", response.data.results[0].admin_id);
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
    cancel() {
      this.$Message.info("取消编辑");
    },
    createProjectOk() {
      this.$refs.CreateProject.addProject(this.search);
    }
  },
  components: {
    CreateProject
  }
};
</script>