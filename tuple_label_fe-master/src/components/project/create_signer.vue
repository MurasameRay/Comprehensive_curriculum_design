<template>
  <div style="width:430px">
    <div>
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
    </div>
  </div>
</template>
<script>
const axios = require("axios");
import urlSetting from "../../setting";
// import Project_List_Manager from "./project_list_manager.vue"
export default {
  data() {
    return {
        columns: [
        {
          title: "User_ID",
          key: "id",
          width: "107px"
        },
        {
          title: "Name",
          key: "name",
          width: "107px"
        },
        {
          title: "User_Name",
          key: "username",
          width: "107px"
        },
        {
          title: "操作",
          key: "action",
          width: 107,
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
        admin_id:"",
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
    addSigner(row) {
      row.admin_id=localStorage.getItem("admin_id")
      axios
        .put(urlSetting.username_url + row.id + "/", row)
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