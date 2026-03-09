#!/usr/bin/env python3
"""
Test script to verify Nova Research Agent setup
"""

import sys

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✅ Streamlit installed")
    except ImportError:
        print("❌ Streamlit not installed")
        return False
    
    try:
        import boto3
        print("✅ Boto3 installed")
    except ImportError:
        print("❌ Boto3 not installed")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print("✅ BeautifulSoup4 installed")
    except ImportError:
        print("❌ BeautifulSoup4 not installed")
        return False
    
    try:
        from duckduckgo_search import DDGS
        print("✅ DuckDuckGo Search installed")
    except ImportError:
        print("❌ DuckDuckGo Search not installed")
        return False
    
    return True

def test_config():
    """Test if configuration is set up"""
    print("\nTesting configuration...")
    
    try:
        import config
        print("✅ Config module loaded")
        
        if config.AWS_ACCESS_KEY_ID and config.AWS_ACCESS_KEY_ID != "your_access_key_here":
            print("✅ AWS credentials configured")
            return True
        else:
            print("⚠️  AWS credentials not set - Will run in DEMO MODE")
            print("   This is OK for testing! Configure .env for real Nova AI.")
            return True  # Still pass, demo mode is valid
        
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def test_modules():
    """Test if custom modules load correctly"""
    print("\nTesting custom modules...")
    
    try:
        from nova_client import NovaClient
        print("✅ NovaClient module loaded")
    except Exception as e:
        print(f"❌ NovaClient error: {e}")
        return False
    
    try:
        from research_engine import ResearchEngine
        print("✅ ResearchEngine module loaded")
    except Exception as e:
        print(f"❌ ResearchEngine error: {e}")
        return False
    
    return True

def test_aws_connection():
    """Test AWS Bedrock connection"""
    print("\nTesting AWS connection...")
    
    try:
        import boto3
        import config
        from demo_mode import is_demo_mode
        
        if is_demo_mode():
            print("⚠️  Running in DEMO MODE (no AWS credentials)")
            print("   App will work with sample data")
            print("   Configure .env for real Nova AI")
            return True
        
        client = boto3.client(
            'bedrock-runtime',
            region_name=config.AWS_REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
        
        print("✅ AWS Bedrock client created")
        print("⚠️  Note: Actual Nova model access not tested (requires API call)")
        return True
        
    except Exception as e:
        print(f"⚠️  AWS connection issue: {e}")
        print("   App will run in DEMO MODE")
        return True  # Still pass, demo mode works

def main():
    """Run all tests"""
    print("🔬 Nova Research Agent - Setup Test\n")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("Configuration", test_config),
        ("Custom Modules", test_modules),
        ("AWS Connection", test_aws_connection),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
        
        print()
    
    print("=" * 50)
    print("\nTest Summary:")
    print("-" * 50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if not result:
            all_passed = False
    
    print("-" * 50)
    
    if all_passed:
        print("\n🎉 All tests passed! You're ready to run the app.")
        print("\n" + "="*50)
        print("NEXT STEPS:")
        print("="*50)
        
        from demo_mode import is_demo_mode
        if is_demo_mode():
            print("\n📝 DEMO MODE DETECTED")
            print("   Run: streamlit run app.py")
            print("   App will work with sample data")
            print("\n   To use real Nova AI:")
            print("   1. Create .env file: cp .env.example .env")
            print("   2. Add your AWS credentials to .env")
            print("   3. Enable Nova access in AWS Bedrock")
        else:
            print("\n✅ AWS CONFIGURED")
            print("   Run: streamlit run app.py")
            print("   App will use real Amazon Nova AI")
        
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        print("\nCommon fixes:")
        print("1. Run: pip install -r requirements.txt")
        print("2. Create .env file with AWS credentials")
        print("3. Ensure AWS Bedrock access is enabled")
        return 1

if __name__ == "__main__":
    sys.exit(main())
