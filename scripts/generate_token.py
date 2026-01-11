#!/usr/bin/env python3
"""Interactive script to help generate GitHub tokens."""
import sys


def main():
    print("🔑 GitHub Token Generator Helper")
    print("=" * 50)
    print()
    print("To create a GitHub Personal Access Token:")
    print()
    print("1. Go to: https://github.com/settings/tokens/new")
    print("2. Set a descriptive name (e.g., 'GitHub Architect Server')")
    print("3. Select the following scopes:")
    print("   ✓ repo (Full control of private repositories)")
    print("   ✓ read:org (Read org and team membership)")
    print("   ✓ user:email (Access user email addresses)")
    print("4. Click 'Generate token'")
    print("5. Copy the token (it starts with 'ghp_')")
    print()
    print("⚠️  Keep your token secure!")
    print("   - Never commit it to version control")
    print("   - Store it in .env file or secrets manager")
    print("   - Rotate it regularly")
    print()
    
    token = input("Paste your token here (or press Enter to skip): ").strip()
    
    if token:
        # Basic validation
        if token.startswith("ghp_") and len(token) >= 40:
            print()
            print("✓ Token format looks valid!")
            print()
            print("Add this to your .env file:")
            print(f"GITHUB_TOKEN={token}")
        else:
            print()
            print("⚠️  Token format doesn't look right.")
            print("   GitHub tokens usually start with 'ghp_' and are 40+ characters")
    else:
        print()
        print("No token provided. Come back when you have one!")
    
    print()


if __name__ == "__main__":
    main()
