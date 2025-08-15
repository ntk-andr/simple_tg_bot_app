import uvicorn
uvicorn.run(
    app='admin.app.app:app',
    host='0.0.0.0'
)
