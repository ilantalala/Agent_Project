# Hebrew AI Customer Service Chat Widget
# Video link: <https://www.loom.com/share/103b0c6c42714628b17333cf85990d64>
A full-stack AI-powered customer service chatbot with conversation history, built with React and FastAPI.

## Features

- **Conversational AI**: GPT-powered Hebrew customer service agent
- **Conversation History**: Maintains context across multiple messages
- **Excel Logging**: All conversations automatically saved to Excel
- **Multiple Models**: Support for GPT-4o, GPT-4o-mini, and GPT-3.5-turbo
- **Customizable**: Configure system prompts and behavior
- **RTL Support**: Full right-to-left Hebrew interface
- **Persistent Settings**: LocalStorage saves user preferences
- **Error Handling**: Comprehensive validation and error messages

## Tech Stack

**Frontend:**
- React 18+ with Hooks
- Axios for API calls
- CSS3 with animations

**Backend:**
- FastAPI (Python 3.8+)
- OpenAI API
- openpyxl for Excel logging
- Pydantic for validation

## Quick Start

### Prerequisites

- Node.js 16+
- Python 3.11
- OpenAI API key

### Backend Setup

```bash
cd Backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload

```

Server runs on http://localhost:8000

### Frontend Setup

```bash
cd Frontend/ai-chat-frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

App runs on http://localhost:5173

## Project Structure

```
AGENT_PROJECT/
├── Backend/
│   ├── main.py           # FastAPI server
│   ├── ai.py             # OpenAI integration
│   ├── models.py         # Pydantic models
│   ├── excel_logger.py   # Excel conversation logger
│   ├── .env              # API keys (create this)
│   └── conversations.xlsx # Auto-generated logs
│
└── Frontend/ai-chat-frontend/
    └── src/
        └── components/
            ├── ChatWidget.jsx  # Main React component
            └── ChatWidget.css  # Styling
```

## API Endpoints

### POST /chat

Send a message and get AI response.

**Request:**
```json
{
  "name": "John Doe",
  "phone": "0501234567",
  "model": "gpt-4o-mini",
  "system_prompt": "Custom prompt (optional)",
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

**Response:**
```json
{
  "reply": "AI response here"
}
```

## Configuration

### Supported Models

- `gpt-4o-mini` - Fast and cost-effective (default)
- `gpt-4o` - Most capable, slower
- `gpt-3.5-turbo` - Basic, fastest

### Custom System Prompt

Override default behavior by providing a custom system prompt in settings or via API.

### Environment Variables

Create `.env` in Backend folder:
```
OPENAI_API_KEY=sk-...
```

## Usage

1. Enter your name and phone number
2. Type a message and press Enter or click send
3. View AI responses in real-time
4. Click ⚙️ to configure model and system prompt
5. Click 🗑️ to clear conversation history

All conversations are automatically logged to `conversations.xlsx`

## Excel Logging

Conversations are saved with:
- Timestamp
- User name
- Phone number
- Full conversation history
- Model used

File location: `Backend/conversations.xlsx`

## Error Handling

The app handles:
- Network failures
- Rate limiting
- Invalid inputs
- Server errors
- Connection timeouts

All errors display user-friendly Hebrew messages.

## Customization

### Change API URL

In settings panel, update the server URL (default: `http://localhost:8000`)

### Modify Default Prompt

Edit `DEFAULT_SYSTEM_PROMPT` in `Backend/ai.py`

### Styling

Modify `ChatWidget.css` for colors, layout, and animations.

## Production Deployment

### Backend

```bash
pip install gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
npm run build
# Serve the dist/ folder with nginx or similar
```

### Security Notes

- Add proper CORS origins in production
- Use environment variables for API keys
- Implement rate limiting
- Add authentication if needed
- Use HTTPS in production

## Troubleshooting

**"Connection Error"**
- Check backend is running on port 8000
- Verify CORS settings
- Check firewall/network settings

**"Rate Limit Error"**
- Wait a few minutes
- Check OpenAI usage limits
- Consider upgrading API tier

**Excel Logging Fails**
- Ensure write permissions
- Close Excel file if open
- Check disk space

## Dependencies

**Backend:**
```
fastapi>=0.104.0
uvicorn>=0.24.0
openai>=1.3.0
python-dotenv>=1.0.0
openpyxl>=3.1.0
pydantic>=2.0.0
```

**Frontend:**
```
react>=18.2.0
axios>=1.6.0
```

## License

MIT

## Support

For issues or questions, check:
- OpenAI API status: https://status.openai.com
- FastAPI docs: https://fastapi.tiangolo.com
- React docs: https://react.dev
