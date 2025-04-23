from database.connection import init_db, search_queries, generated_pages
from database.operations import (
    save_search_query,
    get_recent_search_results,
    save_generated_page,
    get_generated_page
)

def test_database():
    # Initialize database
    init_db()
    
    # Test search query operations
    test_query = "test search query"
    test_results = [
        {"title": "Test Result 1", "snippet": "This is a test snippet", "url": "http://test1.com"},
        {"title": "Test Result 2", "snippet": "Another test snippet", "url": "http://test2.com"}
    ]
    
    # Save a test query
    save_search_query(test_query, test_results)
    print("✅ Saved test search query")
    
    # Retrieve the test query
    retrieved_results = get_recent_search_results(test_query)
    print("✅ Retrieved test search query")
    print(f"Results: {retrieved_results}")
    
    # Test page operations
    test_url = "http://test.com"
    test_content = "<html><body>Test content</body></html>"
    
    # Save a test page
    save_generated_page(test_url, test_content)
    print("✅ Saved test page")
    
    # Retrieve the test page
    retrieved_content = get_generated_page(test_url)
    print("✅ Retrieved test page")
    print(f"Content: {retrieved_content}")
    
    # Clean up test data
    search_queries.delete_many({"query": test_query})
    generated_pages.delete_many({"url": test_url})
    print("✅ Cleaned up test data")

if __name__ == "__main__":
    test_database() 