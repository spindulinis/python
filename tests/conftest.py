import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import text

from main import app
from api.deps import get_db
from core.config import settings

TEST_DB_NAME = "nestjs_test"
TEST_SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_SERVER}:{settings.MYSQL_PORT}/{TEST_DB_NAME}"

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """
    Creates the 'fastapi_test' database if it doesn't exist, 
    and drops it when all tests are finished.
    """
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)
    
    # Create tables
    SQLModel.metadata.create_all(engine)
    
    yield
    
    # Optional: Drop the database after tests are done
    # drop_database(engine.url)

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URI)
    
    with Session(engine) as session:
        # 1. Clear the data before the test starts
        session.exec(text("SET FOREIGN_KEY_CHECKS = 0;"))
        
        # Get all table names registered in your SQLModel metadata
        for table in reversed(SQLModel.metadata.sorted_tables):
            session.exec(text(f"TRUNCATE TABLE {table.name};"))
            
        session.exec(text("SET FOREIGN_KEY_CHECKS = 1;"))
        session.commit()
        
        yield session
        
        # 2. Optional: rollback after test to ensure no hanging transactions
        session.rollback()

@pytest.fixture(name="client")
def client_fixture(session: Session):
    """
    Overrides the 'get_db' dependency in FastAPI to use our test session.
    """
    def get_session_override():
        yield session
    
    app.dependency_overrides[get_db] = get_session_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()