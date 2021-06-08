let host = window.location.host+':8000'

const urlSettings = {
    project_url: `http://${host}/api/project/`,
    label_url: `http://${host}/api/label/`,
    document_url: `http://${host}/api/document/`,
    annotation_url: `http://${host}/api/annotation/`,
    status_url: `http://${host}/api/project_status/`,
    project_import_url: `http://${host}/api/project_import/`,
    project_export_url: `http://${host}/api/project_export/`,
    username_url: `http://${host}/api/signer/`,
    admin_url:`http://${host}/api/admin/`,
}

export default urlSettings;