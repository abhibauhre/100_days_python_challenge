# ==================== PERSONAL FINANCE TRACKER ====================
# Mini Project using: Lists, Dictionaries, Functions, File Handling, Date/Time, Math

import json
import os
from datetime import datetime, timedelta
import calendar

print("💰 PERSONAL FINANCE TRACKER")
print("="*50)

# ==================== DATA STRUCTURES ====================

# List to store all transactions
transactions = []

# Dictionary for expense categories
expense_categories = {
    "FOOD": "Food & Dining",
    "TRANSPORT": "Transportation", 
    "BILLS": "Bills & Utilities",
    "SHOPPING": "Shopping",
    "HEALTH": "Healthcare",
    "ENTERTAINMENT": "Entertainment",
    "EDUCATION": "Education",
    "OTHER": "Other"
}

# Dictionary for income sources
income_sources = {
    "SALARY": "Salary",
    "FREELANCE": "Freelance Work",
    "BUSINESS": "Business Income",
    "INVESTMENT": "Investment Returns",
    "GIFT": "Gift/Bonus",
    "OTHER": "Other Income"
}

# Budget limits for categories (monthly)
monthly_budgets = {
    "FOOD": 5000,
    "TRANSPORT": 2000,
    "BILLS": 3000,
    "SHOPPING": 2500,
    "HEALTH": 1500,
    "ENTERTAINMENT": 2000,
    "EDUCATION": 1000,
    "OTHER": 1000
}

# ==================== FUNCTIONS ====================

def add_transaction():
    """Add a new income or expense transaction"""
    print("\n💳 ADD NEW TRANSACTION")
    print("-" * 25)
    
    # Choose transaction type
    while True:
        trans_type = input("Transaction type (income/expense): ").lower().strip()
        if trans_type in ['income', 'expense']:
            break
        print("❌ Please enter 'income' or 'expense'!")
    
    # Get amount
    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            if amount > 0:
                break
            print("❌ Amount must be positive!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Get description
    description = input("Enter description: ").strip()
    if not description:
        description = "No description"
    
    # Get category/source
    if trans_type == 'expense':
        print("\nExpense Categories:")
        for code, name in expense_categories.items():
            print(f"  {code}: {name}")
        
        while True:
            category = input("Choose category code: ").upper().strip()
            if category in expense_categories:
                break
            print("❌ Invalid category code!")
        
        category_name = expense_categories[category]
    
    else:  # income
        print("\nIncome Sources:")
        for code, name in income_sources.items():
            print(f"  {code}: {name}")
        
        while True:
            category = input("Choose source code: ").upper().strip()
            if category in income_sources:
                break
            print("❌ Invalid source code!")
        
        category_name = income_sources[category]
    
    # Get date (optional)
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_input:
            transaction_date = datetime.now().strftime("%Y-%m-%d")
            break
        
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            transaction_date = date_input
            break
        except ValueError:
            print("❌ Invalid date format! Use YYYY-MM-DD")
    
    # Create transaction tuple
    transaction = {
        'id': len(transactions) + 1,
        'type': trans_type,
        'amount': amount,
        'description': description,
        'category': category,
        'category_name': category_name,
        'date': transaction_date,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    transactions.append(transaction)
    print(f"✅ {trans_type.title()} of ₹{amount} added successfully!")

def view_transactions():
    """Display all transactions with filtering options"""
    if not transactions:
        print("\n❌ No transactions found!")
        return
    
    print("\n📊 VIEW TRANSACTIONS")
    print("-" * 20)
    print("1. All transactions")
    print("2. Income only")
    print("3. Expenses only")
    print("4. By category")
    print("5. By date range")
    
    while True:
        choice = input("Choose option (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            break
        print("❌ Please enter 1-5!")
    
    filtered_transactions = []
    
    if choice == '1':
        filtered_transactions = transactions
    
    elif choice == '2':
        filtered_transactions = [t for t in transactions if t['type'] == 'income']
    
    elif choice == '3':
        filtered_transactions = [t for t in transactions if t['type'] == 'expense']
    
    elif choice == '4':
        print("\nAvailable categories:")
        all_categories = set()
        for t in transactions:
            all_categories.add(t['category'])
        
        for cat in sorted(all_categories):
            print(f"  {cat}")
        
        filter_category = input("Enter category code: ").upper().strip()
        filtered_transactions = [t for t in transactions if t['category'] == filter_category]
    
    elif choice == '5':
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        
        filtered_transactions = [
            t for t in transactions 
            if start_date <= t['date'] <= end_date
        ]
    
    if not filtered_transactions:
        print("❌ No transactions match your criteria!")
        return
    
    # Display transactions
    print(f"\n📋 TRANSACTIONS ({len(filtered_transactions)} found)")
    print("="*80)
    print(f"{'ID':<4} {'Date':<12} {'Type':<8} {'Amount':<10} {'Category':<15} {'Description':<25}")
    print("-"*80)
    
    total_income = 0
    total_expense = 0
    
    for trans in sorted(filtered_transactions, key=lambda x: x['date'], reverse=True):
        amount_str = f"₹{trans['amount']:.2f}"
        print(f"{trans['id']:<4} {trans['date']:<12} {trans['type']:<8} {amount_str:<10} {trans['category']:<15} {trans['description']:<25}")
        
        if trans['type'] == 'income':
            total_income += trans['amount']
        else:
            total_expense += trans['amount']
    
    print("-"*80)
    print(f"💰 Total Income: ₹{total_income:.2f}")
    print(f"💸 Total Expense: ₹{total_expense:.2f}")
    print(f"💵 Net Amount: ₹{total_income - total_expense:.2f}")

def monthly_report():
    """Generate monthly financial report"""
    if not transactions:
        print("\n❌ No transactions found!")
        return
    
    # Get current month or let user choose
    current_month = datetime.now().strftime("%Y-%m")
    month_input = input(f"Enter month (YYYY-MM) or press Enter for current ({current_month}): ").strip()
    
    if not month_input:
        report_month = current_month
    else:
        try:
            datetime.strptime(month_input, "%Y-%m")
            report_month = month_input
        except ValueError:
            print("❌ Invalid month format!")
            return
    
    # Filter transactions for the month
    month_transactions = [
        t for t in transactions 
        if t['date'].startswith(report_month)
    ]
    
    if not month_transactions:
        print(f"❌ No transactions found for {report_month}!")
        return
    
    print(f"\n📅 MONTHLY REPORT - {report_month}")
    print("="*50)
    
    # Calculate totals
    total_income = sum(t['amount'] for t in month_transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in month_transactions if t['type'] == 'expense')
    net_savings = total_income - total_expense
    
    print(f"💰 Total Income: ₹{total_income:.2f}")
    print(f"💸 Total Expense: ₹{total_expense:.2f}")
    print(f"💵 Net Savings: ₹{net_savings:.2f}")
    
    if total_income > 0:
        savings_rate = (net_savings / total_income) * 100
        print(f"📈 Savings Rate: {savings_rate:.1f}%")
    
    # Category-wise expense breakdown
    print(f"\n💸 EXPENSE BREAKDOWN:")
    print("-" * 30)
    
    category_expenses = {}
    for trans in month_transactions:
        if trans['type'] == 'expense':
            category = trans['category']
            category_expenses[category] = category_expenses.get(category, 0) + trans['amount']
    
    for category, amount in sorted(category_expenses.items(), key=lambda x: x[1], reverse=True):
        category_name = expense_categories.get(category, category)
        percentage = (amount / total_expense * 100) if total_expense > 0 else 0
        budget = monthly_budgets.get(category, 0)
        
        status = "✅" if amount <= budget else "⚠️"
        print(f"{status} {category_name}: ₹{amount:.2f} ({percentage:.1f}%) [Budget: ₹{budget}]")
    
    # Income source breakdown
    print(f"\n💰 INCOME BREAKDOWN:")
    print("-" * 30)
    
    income_sources_amounts = {}
    for trans in month_transactions:
        if trans['type'] == 'income':
            source = trans['category']
            income_sources_amounts[source] = income_sources_amounts.get(source, 0) + trans['amount']
    
    for source, amount in sorted(income_sources_amounts.items(), key=lambda x: x[1], reverse=True):
        source_name = income_sources.get(source, source)
        percentage = (amount / total_income * 100) if total_income > 0 else 0
        print(f"💼 {source_name}: ₹{amount:.2f} ({percentage:.1f}%)")
    
    # Budget analysis
    print(f"\n📊 BUDGET ANALYSIS:")
    print("-" * 30)
    
    total_budget = sum(monthly_budgets.values())
    budget_used = sum(category_expenses.values())
    budget_remaining = total_budget - budget_used
    
    print(f"📋 Total Monthly Budget: ₹{total_budget:.2f}")
    print(f"💸 Budget Used: ₹{budget_used:.2f}")
    print(f"💰 Budget Remaining: ₹{budget_remaining:.2f}")
    
    if total_budget > 0:
        budget_usage_rate = (budget_used / total_budget) * 100
        print(f"📈 Budget Usage: {budget_usage_rate:.1f}%")
        
        if budget_usage_rate > 100:
            print("⚠️ WARNING: You've exceeded your total budget!")
        elif budget_usage_rate > 80:
            print("⚠️ CAUTION: You're using 80%+ of your budget!")
        else:
            print("✅ Good! You're within budget limits.")

def set_budget():
    """Set or update budget limits for categories"""
    print("\n💰 SET MONTHLY BUDGETS")
    print("-" * 25)
    
    print("Current budgets:")
    for category, budget in monthly_budgets.items():
        category_name = expense_categories[category]
        print(f"  {category_name}: ₹{budget}")
    
    print("\nUpdate budgets (press Enter to keep current):")
    
    for category, category_name in expense_categories.items():
        current_budget = monthly_budgets[category]
        while True:
            new_budget = input(f"{category_name} (current: ₹{current_budget}): ").strip()
            
            if not new_budget:
                break
            
            try:
                budget_amount = float(new_budget)
                if budget_amount >= 0:
                    monthly_budgets[category] = budget_amount
                    print(f"✅ Updated {category_name} budget to ₹{budget_amount}")
                    break
                else:
                    print("❌ Budget must be positive!")
            except ValueError:
                print("❌ Please enter a valid number!")

def export_data():
    """Export transactions to CSV format"""
    if not transactions:
        print("\n❌ No transactions to export!")
        return
    
    filename = f"transactions_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(filename, 'w') as file:
            # Write header
            file.write("ID,Date,Type,Amount,Category,Category_Name,Description,Created_At\n")
            
            # Write transactions
            for trans in transactions:
                file.write(f"{trans['id']},{trans['date']},{trans['type']},{trans['amount']},{trans['category']},{trans['category_name']},\"{trans['description']}\",{trans['created_at']}\n")
        
        print(f"✅ Data exported to {filename}")
    
    except Exception as e:
        print(f"❌ Error exporting data: {e}")

def financial_insights():
    """Provide financial insights and tips"""
    if not transactions:
        print("\n❌ No data available for insights!")
        return
    
    print("\n🔍 FINANCIAL INSIGHTS")
    print("="*30)
    
    # Get last 30 days transactions
    thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    recent_transactions = [t for t in transactions if t['date'] >= thirty_days_ago]
    
    if not recent_transactions:
        print("❌ No recent transactions (last 30 days)")
        return
    
    # Calculate metrics
    recent_income = sum(t['amount'] for t in recent_transactions if t['type'] == 'income')
    recent_expense = sum(t['amount'] for t in recent_transactions if t['type'] == 'expense')
    
    print(f"📊 Last 30 Days Analysis:")
    print(f"   Income: ₹{recent_income:.2f}")
    print(f"   Expense: ₹{recent_expense:.2f}")
    print(f"   Net: ₹{recent_income - recent_expense:.2f}")
    
    # Top spending categories
    category_spending = {}
    for trans in recent_transactions:
        if trans['type'] == 'expense':
            cat = trans['category']
            category_spending[cat] = category_spending.get(cat, 0) + trans['amount']
    
    if category_spending:
        print(f"\n💸 Top Spending Categories:")
        sorted_categories = sorted(category_spending.items(), key=lambda x: x[1], reverse=True)
        for i, (cat, amount) in enumerate(sorted_categories[:3], 1):
            cat_name = expense_categories.get(cat, cat)
            print(f"   {i}. {cat_name}: ₹{amount:.2f}")
    
    # Financial tips
    print(f"\n💡 FINANCIAL TIPS:")
    print("-" * 20)
    
    if recent_income > recent_expense:
        savings_rate = ((recent_income - recent_expense) / recent_income) * 100
        print(f"✅ Great! You're saving {savings_rate:.1f}% of your income")
        
        if savings_rate < 20:
            print("💡 Tip: Try to save at least 20% of your income")
        else:
            print("🏆 Excellent savings rate! Keep it up!")
    
    else:
        deficit = recent_expense - recent_income
        print(f"⚠️ You're spending ₹{deficit:.2f} more than you earn")
        print("💡 Tips to improve:")
        print("   - Review and cut unnecessary expenses")
        print("   - Look for additional income sources")
        print("   - Set stricter budgets for top spending categories")
    
    # Budget alerts
    current_month = datetime.now().strftime("%Y-%m")
    month_expenses = [t for t in transactions if t['date'].startswith(current_month) and t['type'] == 'expense']
    
    month_category_expenses = {}
    for trans in month_expenses:
        cat = trans['category']
        month_category_expenses[cat] = month_category_expenses.get(cat, 0) + trans['amount']
    
    print(f"\n⚠️ BUDGET ALERTS:")
    print("-" * 15)
    
    alerts_found = False
    for cat, spent in month_category_expenses.items():
        budget = monthly_budgets.get(cat, 0)
        if budget > 0:
            usage_percent = (spent / budget) * 100
            if usage_percent > 90:
                cat_name = expense_categories.get(cat, cat)
                print(f"🚨 {cat_name}: {usage_percent:.1f}% of budget used (₹{spent:.2f}/₹{budget})")
                alerts_found = True
    
    if not alerts_found:
        print("✅ No budget alerts - you're doing well!")

def save_data():
    """Save all data to JSON file"""
    try:
        data = {
            'transactions': transactions,
            'monthly_budgets': monthly_budgets,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open('finance_data.json', 'w') as file:
            json.dump(data, file, indent=2)
        
        print("✅ Data saved successfully!")
    
    except Exception as e:
        print(f"❌ Error saving data: {e}")

def load_data():
    """Load data from JSON file"""
    global transactions, monthly_budgets
    
    if not os.path.exists('finance_data.json'):
        print("📝 No previous data found. Starting fresh!")
        return
    
    try:
        with open('finance_data.json', 'r') as file:
            data = json.load(file)
        
        transactions = data.get('transactions', [])
        monthly_budgets.update(data.get('monthly_budgets', {}))
        
        print(f"✅ Loaded {len(transactions)} transactions from file!")
        if 'last_updated' in data:
            print(f"📅 Last updated: {data['last_updated']}")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")

# ==================== MAIN PROGRAM ====================

def main():
    """Main program loop"""
    load_data()
    
    while True:
        print("\n" + "="*50)
        print("💰 PERSONAL FINANCE TRACKER")
        print("="*50)
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Monthly Report")
        print("4. Set Budget")
        print("5. Financial Insights")
        print("6. Export Data")
        print("7. Save Data")
        print("8. Exit")
        print("-"*50)
        
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            monthly_report()
        elif choice == '4':
            set_budget()
        elif choice == '5':
            financial_insights()
        elif choice == '6':
            export_data()
        elif choice == '7':
            save_data()
        elif choice == '8':
            save_data()  # Auto-save before exit
            print("\n👋 Thank you for using Personal Finance Tracker!")
            print("💡 Remember: Track regularly for better financial health!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-8.")

# ==================== DEMO DATA ====================

def add_demo_data():
    """Add demo transactions for testing"""
    demo_transactions = [
        {'id': 1, 'type': 'income', 'amount': 50000, 'description': 'Monthly Salary', 'category': 'SALARY', 'category_name': 'Salary', 'date': '2024-10-01', 'created_at': '2024-10-01 09:00:00'},
        {'id': 2, 'type': 'expense', 'amount': 1500, 'description': 'Groceries', 'category': 'FOOD', 'category_name': 'Food & Dining', 'date': '2024-10-02', 'created_at': '2024-10-02 10:30:00'},
        {'id': 3, 'type': 'expense', 'amount': 800, 'description': 'Metro Card Recharge', 'category': 'TRANSPORT', 'category_name': 'Transportation', 'date': '2024-10-03', 'created_at': '2024-10-03 08:15:00'},
        {'id': 4, 'type': 'expense', 'amount': 2500, 'description': 'Electricity Bill', 'category': 'BILLS', 'category_name': 'Bills & Utilities', 'date': '2024-10-04', 'created_at': '2024-10-04 14:20:00'},
        {'id': 5, 'type': 'income', 'amount': 5000, 'description': 'Freelance Project', 'category': 'FREELANCE', 'category_name': 'Freelance Work', 'date': '2024-10-05', 'created_at': '2024-10-05 16:45:00'},
        {'id': 6, 'type': 'expense', 'amount': 1200, 'description': 'Movie & Dinner', 'category': 'ENTERTAINMENT', 'category_name': 'Entertainment', 'date': '2024-10-06', 'created_at': '2024-10-06 20:30:00'}
    ]
    
    transactions.extend(demo_transactions)
    print("✅ Demo data added!")

# ==================== PROGRAM START ====================

if __name__ == "__main__":
    print("🚀 Welcome to Personal Finance Tracker!")
    print("="*50)
    print("💡 Track your income and expenses to achieve financial goals!")
    
    # Ask if user wants demo data
    if not transactions:
        demo = input("\nWould you like to add demo data for testing? (y/n): ").lower()
        if demo == 'y':
            add_demo_data()
    
    main()

print("\n🎉 Program completed successfully!")
print("abhi")