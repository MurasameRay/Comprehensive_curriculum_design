<template>
  <div>
    <Row>
      <Col span="1">
      <Button
        @click="createProjectOption.isShow = true"
        type="success"
      >新增标注员</Button>
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
        <FormItem label="Signer Name">
          <Input v-model="editData.name" />
        </FormItem>
        <FormItem label="Description">
          <Input v-model="editData.description" />
        </FormItem>
      </Form>
    </Modal>

    <Modal
      v-model="createProjectOption.isShow"
      title="新增标注员"
      @on-ok="createProjectOk"
      @on-cancel="createProjectOption.isShow = false"
    >
      <CreateProject ref="CreateProject"></CreateProject>
    </Modal>
  </div>

</template>
<script>
const axios = require("axios");
import urlSetting from "../../setting";
import CreateProject from "../project/create_signer";
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
          title: "Signer Name",
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
         
            ]);
          }
        }
      ],
      data1: [],
      editData: {
        id: "",
        name: "",
        description: ""
      },
      createProjectOption: {
        isShow: false
      }
    };
  },
  mounted() {
    this.search();
  },
  methods: {
    search() {
      axios
        .get(urlSetting.project_url)
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            this.data1 = response.data.results;
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
    deleteProject(row) {
      axios
        .delete(urlSetting.project_url + row.id + "/")
        .then(response => {
          console.log(response);
          if (response.status === 204) {
            this.$Message.success("删除成功");
            this.search();
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
    createProjectOk() {
      this.$refs.CreateProject.addProject(this.search);
    }
  },
  components: {
    CreateProject
  }
};
</script>