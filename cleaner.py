from googleapiclient.discovery import build
from auth import get_credentials
import sys

def create_service():
    """Create Gmail API service"""
    creds = get_credentials()
    if not creds:
        return None
    
    service = build('gmail', 'v1', credentials=creds)
    return service

def search_messages(service, query):
    """
    Search for messages matching the query
    Returns a list of message IDs
    """
    result_ids = []
    page_token = None
    
    while True:
        try:
            results = service.users().messages().list(
                userId='me', 
                q=query, 
                pageToken=page_token,
                maxResults=500  # Max allowed per page
            ).execute()
            
            messages = results.get('messages', [])
            
            if not messages:
                break
                
            for msg in messages:
                result_ids.append(msg['id'])
                
            page_token = results.get('nextPageToken')
            if not page_token:
                break
                
            print(f"Found {len(result_ids)} emails so far...", end='\r')
            
        except Exception as e:
            print(f"An error occurred during search: {e}")
            break
            
    return result_ids

def batch_delete_messages(service, message_ids):
    """
    Delete messages in batches of 1000 (API limit)
    """
    if not message_ids:
        print("No messages to delete.")
        return 0
        
    total_deleted = 0
    batch_size = 1000
    
    print(f"\nProcessing {len(message_ids)} emails for deletion...")
    
    for i in range(0, len(message_ids), batch_size):
        batch = message_ids[i:i + batch_size]
        
        try:
            service.users().messages().batchDelete(
                userId='me',
                body={'ids': batch}
            ).execute()
            
            total_deleted += len(batch)
            print(f"Deleted {total_deleted}/{len(message_ids)} emails...", end='\r')
            
        except Exception as e:
            print(f"\nError deleting batch: {e}")
            
    print(f"\nSuccessfully deleted {total_deleted} emails.")
    return total_deleted

def get_category_query(category):
    """Map user friendly category to Gmail query"""
    categories = {
        'promotions': 'category:promotions',
        'social': 'category:social',
        'updates': 'category:updates',
        'forums': 'category:forums',
        'trash': 'in:trash',
        'spam': 'in:spam'
    }
    return categories.get(category.lower())
