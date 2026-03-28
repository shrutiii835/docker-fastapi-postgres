from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
from tenacity import retry, stop_after_attempt, wait_exponential
from app.core.config import settings

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())

# Lazy engine creation with retry
def get_engine():
    @retry(stop=stop_after_attempt(15), wait=wait_exponential(multiplier=1, min=1, max=10))
    def create_db_engine():
        engine = create_engine(
            settings.DATABASE_URL,
            echo=False,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20
        )
        # Test connection
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return engine
    return create_db_engine()

# Session factory (will be created when needed)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)

def get_db():
    # Lazy bind the engine when first used
    if not SessionLocal.kw.get("bind"):
        engine = get_engine()
        SessionLocal.configure(bind=engine)
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
