module.exports = {
    apps: [
      {
        name: "web_payment_api",
        script: "main.py",
        autorestart: true,
        watch: false,
        ignore_watch: ["logs", "venv"],
        max_memory_restart: "1G",
        log_date_format: "YYYY-MM-DD HH:mm Z",
        out_file: "logs/out.log",
        error_file: "logs/error.log",
        merge_logs: true,
        max_size: "10M",
        max_files: 5,
      },
    ],
  };