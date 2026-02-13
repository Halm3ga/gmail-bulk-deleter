import sys
from datetime import datetime, timedelta
from cleaner import create_service, search_messages, batch_delete_messages, get_category_query

def main():
    print("="*60)
    print("      GMAIL BULK DELETER - CLEAN YOUR INBOX")
    print("="*60)
    
    # 1. Connect to Gmail
    print("\nConnecting to Gmail...")
    service = create_service()
    if not service:
        input("\nPress Enter to exit...")
        sys.exit(1)
    print("✅ Connected successfully!")
    
    # 2. Get User Input
    print("\n--- Filter Options ---")
    print("1. Delete emails older than X days")
    print("2. Delete emails by category (Promotions, Social, etc.)")
    print("3. Custom query")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    query = ""
    
    if choice == '1':
        days = input("Enter number of days (e.g., 365 for 1 year old): ").strip()
        if not days.isdigit():
            print("Invalid input.")
            sys.exit(1)
        
        # Calculate date
        cutoff_date = datetime.now() - timedelta(days=int(days))
        date_str = cutoff_date.strftime("%Y/%m/%d")
        query = f"before:{date_str}"
        print(f"Looking for emails older than: {date_str}")
        
    elif choice == '2':
        print("\nCategories: promotions, social, updates, forums, spam, trash")
        cat = input("Enter category: ").strip().lower()
        query = get_category_query(cat)
        if not query:
            print("Invalid category.")
            sys.exit(1)
            
    elif choice == '3':
        query = input("Enter custom Gmail search query (e.g., 'from:amazon label:read'): ")
        
    else:
        print("Invalid choice.")
        sys.exit(1)
        
    # Add safety filter to avoid deleting starred/important unless specified
    if 'in:trash' not in query and 'in:spam' not in query:
        exclude_important = input("\nExclude 'Starred' and 'Important' emails? (y/n): ").lower()
        if exclude_important == 'y':
            query += " -is:starred -is:important"
    
    print(f"\nFinal Query: [{query}]")
    
    # 3. Search Loop
    print("\nSearching for emails...")
    ids = search_messages(service, query)
    
    if not ids:
        print("🎉 No emails found matching criteria!")
        input("\nPress Enter to exit...")
        sys.exit(0)
        
    print(f"\n⚠️ FOUND {len(ids)} EMAILS MATCHING YOUR CRITERIA")
    
    # 4. Confirmation
    confirm = input("\nType 'DELETE' to permanently delete these emails (or anything else to cancel): ")
    
    if confirm == 'DELETE':
        batch_delete_messages(service, ids)
    else:
        print("\nOperation cancelled. No emails were deleted.")
        
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
