# 🏛️ LawGic AI - लॉजिक AI - Integrated Legal Assistant

A comprehensive AI-powered legal assistance platform that makes law accessible, affordable, and understandable for everyone. Built with **"Rights Over Riches"** philosophy - reimagining fairness for everyone.

## 🎯 **Project Overview**

LawGic AI combines a powerful FastAPI backend with a beautiful React frontend to provide:

- **🤖 Smart Legal Analysis**: AI-powered document and query analysis
- **📁 Multi-Input Support**: Text, document uploads, and voice processing  
- **📋 Structured Legal Guidance**: Categorized advice with actionable recommendations
- **🌍 Multilingual Support**: Full English and Hindi (हिंदी) interface with seamless translation
- **🎭 Demo Mode**: Fully functional without requiring trained ML models
- **🔒 Privacy First**: End-to-end encryption and automatic PII redaction

## 📁 **Project Structure**

```
final-Lawgic/
├── backend/                    # FastAPI backend service
│   ├── app/                   # Main application code
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Core configurations
│   │   ├── db/               # Database models & setup
│   │   └── services/         # Business logic services
│   ├── init_db.py            # Database initialization
│   └── requirements.txt      # Python dependencies
├── frontend/                  # React + Vite frontend
│   ├── src/                  # Source code
│   │   ├── components/       # Reusable UI components
│   │   ├── contexts/         # React contexts (Language)
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   └── i18n.ts          # Internationalization
│   ├── public/              # Static assets
│   └── package.json         # Node.js dependencies
├── render.yml                # Render deployment config
├── scripts/                  # Utility scripts
├── docs/                    # Documentation
└── README.md               # This file
```

## 🚀 **Quick Start**

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn

### 1. Start Backend
```bash
cd backend
pip3 install -r requirements.txt
python3 init_db.py
python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 2. Start Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Access the Application
- **Frontend**: http://localhost:5173 (Vite default)
- **Backend API**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/docs
- **Language Toggle**: Available in header (EN/हिं)

## ✨ **Features**

### 🤖 **AI-Powered Analysis**
- **Contract Law**: Rental agreements, employment contracts, service agreements
- **Tenant Rights**: Landlord-tenant disputes, eviction processes, housing rights
- **Employment Law**: Workplace rights, termination, harassment issues
- **General Legal**: Wide range of legal queries with structured responses

### 📄 **Document Processing**
- **Upload Support**: PDF, DOCX, TXT files
- **Text Extraction**: Intelligent content parsing
- **Combined Analysis**: Text queries + document content

### 🎤 **Voice Support**
- **Audio Formats**: WAV, MP3, M4A, OGG
- **Transcription**: Voice-to-text conversion
- **Integrated Analysis**: Voice + text + documents

### 🌍 **Multilingual Support**
- **Languages**: Full English and Hindi (हिंदी) support
- **UI Translation**: Complete interface translation including headers, footers, legal terms
- **Response Translation**: AI responses formatted with translated headers (Category, Document Summary, Risk Assessment, etc.)
- **Seamless Switching**: Toggle between languages with single click
- **Cultural Context**: Hindi responses with culturally appropriate legal references

### 🔒 **Privacy & Security**
- **Local Processing**: Demo mode works without external APIs
- **Data Protection**: Automatic PII redaction (when enabled)
- **Secure Storage**: SQLite database with proper encryption support
- **End-to-End Encryption**: Industry-standard AES-256 encryption
- **GDPR Compliant**: International privacy standards compliance

## 🛠️ **Technology Stack**

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: Database ORM
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

### Frontend
- **React 18**: Modern UI framework with hooks
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool and dev server
- **Tailwind CSS**: Utility-first styling
- **Shadcn/ui**: Beautiful component library
- **React Router**: Client-side routing
- **i18next**: Internationalization framework
- **Sonner**: Toast notifications
- **Lucide React**: Modern icon library

## 📋 **API Endpoints**

### Core Endpoints
- `GET /`: Welcome message
- `POST /api/predict/`: Simple text analysis
- `POST /api/analyze/`: Multi-input analysis (text + files + voice)

### Example Usage
```bash
# Text analysis
curl -X POST "http://127.0.0.1:8000/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"text": "I need help with my rental agreement"}'

# File analysis
curl -X POST "http://127.0.0.1:8000/api/analyze/" \
  -F "file=@contract.pdf" \
  -F "text=Please analyze this contract"
```

## 🎨 **Frontend Features**

### Main Interface
- **Clean Design**: Modern, accessible UI
- **Responsive**: Works on desktop and mobile
- **Real-time**: Live backend integration

### Chat Interface
- **Conversation Flow**: Natural chat experience
- **File Upload**: Drag-and-drop or button upload
- **Voice Upload**: Audio file processing
- **Structured Responses**: Formatted legal analysis

### Navigation
- **Homepage**: Feature overview and getting started
- **Ask AI**: Main chat interface
- **Responsive Menu**: Mobile-friendly navigation

## 🧪 **Testing the Integration**

### Test Scenarios
1. **Text Query**: "What are my rights as a tenant?" / "किरायेदार के रूप में मेरे अधिकार क्या हैं?"
2. **Language Switching**: Toggle between English and Hindi (हिंदी) using header button
3. **Document Upload**: Upload a rental agreement or contract (.pdf, .docx, .txt)
4. **Voice Upload**: Upload an audio question (.wav, .mp3, .m4a, .ogg)
5. **Combined Analysis**: Text + document + voice analysis
6. **Suggestion Buttons**: Try pre-written legal questions in both languages
7. **Response Translation**: Verify headers like "Category:", "Document Summary:", "Disclaimer" are translated

### Expected Response Format
```json
{
  "input_text": "Combined input from all sources",
  "prediction": {
    "category": "Contract Law",
    "confidence": 0.85,
    "key_points": ["Point 1", "Point 2"],
    "recommendations": ["Rec 1", "Rec 2"],
    "demo_note": "This is a demo response..."
  },
  "document_id": 123
}
```

## 🔧 **Configuration**

### Environment Variables

#### Backend (.env)
```bash
DATABASE_URL=sqlite:///./law_ai_demo.db     # Database connection
AI_API_KEY=your_openai_key                  # Optional: for embeddings
CORS_ORIGINS=http://localhost:5173         # Frontend URL for CORS
ENVIRONMENT=development                     # Environment mode
```

#### Frontend (.env)
```bash
VITE_API_BASE_URL=http://127.0.0.1:8000    # Backend API URL
```

#### Production (Render)
```bash
# Backend
CORS_ORIGINS=https://lawgic-ai-frontend.onrender.com
ENVIRONMENT=production

# Frontend
VITE_API_BASE_URL=https://lawgic-ai-backend.onrender.com
```

### Demo Mode
The application runs in full demo mode without requiring:
- Trained ML models (model.pkl)
- OpenAI API keys
- External dependencies
- Complex setup

## 📚 **Documentation**

- **API Docs**: Available at `/docs` when backend is running
- **Component Docs**: Check `frontend/src/components/`
- **Database Schema**: See `backend/app/db/models.py`

## 🚀 **Deployment**

### 🗺️ Render Deployment (Recommended)

This project includes a `render.yml` configuration file for seamless deployment on Render:

1. **Fork/Clone** this repository to your GitHub account
2. **Connect** your GitHub repository to Render
3. **Deploy** using the provided `render.yml` configuration

The `render.yml` automatically configures:
- **Backend Service**: Python web service with FastAPI
- **Frontend Service**: Static site deployment with Vite build
- **Environment Variables**: Pre-configured for production
- **Health Checks**: Backend health monitoring
- **CORS Configuration**: Proper frontend-backend communication

#### Render Services Created:
- `lawgic-ai-backend` - Python FastAPI service
- `lawgic-ai-frontend` - Static React application

### 💻 Local Development
Both servers include hot-reload for development:
- **Backend**: `--reload` flag with uvicorn
- **Frontend**: Vite dev server with HMR

### 🌐 Manual Production Deployment
For other platforms:
1. **Build frontend**: `npm run build`
2. **Configure environment**: Set production variables
3. **Deploy backend**: Use production ASGI server
4. **Serve static files**: Configure static file serving
5. **Database**: Configure PostgreSQL for production

## 🤝 **Contributing**

1. Fork the project
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 **License**

This project is licensed under the MIT License.

## 💡 **Support**

For issues or questions:
1. Check existing documentation
2. Test with demo data
3. Review API responses
4. Check browser console for frontend issues

---

**Built with ❤️ for accessible legal AI**