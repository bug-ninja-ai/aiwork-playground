#!/usr/bin/env python3
"""
Test script to verify the font size changes for "What is AI Work Playground?" heading.
"""

import re
from pathlib import Path

def test_font_size_changes():
    """Test that the font size changes are correctly implemented."""

    print("🧪 Testing Font Size Changes for 'What is AI Work Playground?' Heading")
    print("=" * 70)

    # Read the HTML file
    html_file = Path("index.html")
    if not html_file.exists():
        print("❌ FAIL: index.html file not found")
        return False

    content = html_file.read_text()

    tests_passed = 0
    total_tests = 0

    def check_requirement(description, condition):
        nonlocal tests_passed, total_tests
        total_tests += 1
        if condition:
            print(f"✅ PASS: {description}")
            tests_passed += 1
        else:
            print(f"❌ FAIL: {description}")

    # Test 1: Desktop font size (35px = 2.1875rem)
    desktop_font_pattern = r'\.section h2\s*\{[^}]*font-size:\s*2\.1875rem'
    check_requirement(
        "Desktop font size is 2.1875rem (35px)",
        re.search(desktop_font_pattern, content, re.DOTALL) is not None
    )

    # Test 2: Desktop line height (42px = 2.625rem)
    desktop_line_height_pattern = r'\.section h2\s*\{[^}]*line-height:\s*2\.625rem'
    check_requirement(
        "Desktop line height is 2.625rem (42px)",
        re.search(desktop_line_height_pattern, content, re.DOTALL) is not None
    )

    # Test 3: Tablet breakpoint exists
    tablet_breakpoint_pattern = r'@media\s*\(max-width:\s*1024px\)\s*and\s*\(min-width:\s*769px\)'
    check_requirement(
        "Tablet breakpoint (769px-1024px) exists",
        re.search(tablet_breakpoint_pattern, content) is not None
    )

    # Test 4: Tablet font size (28px = 1.75rem)
    tablet_font_pattern = r'@media\s*\(max-width:\s*1024px\)\s*and\s*\(min-width:\s*769px\)[^}]*\.section h2\s*\{[^}]*font-size:\s*1\.75rem'
    check_requirement(
        "Tablet font size is 1.75rem (28px)",
        re.search(tablet_font_pattern, content, re.DOTALL) is not None
    )

    # Test 5: Tablet line height (34px = 2.125rem)
    tablet_line_height_pattern = r'@media\s*\(max-width:\s*1024px\)\s*and\s*\(min-width:\s*769px\)[^}]*\.section h2\s*\{[^}]*line-height:\s*2\.125rem'
    check_requirement(
        "Tablet line height is 2.125rem (34px)",
        re.search(tablet_line_height_pattern, content, re.DOTALL) is not None
    )

    # Test 6: Mobile font size (24px = 1.5rem)
    # Find the mobile media query block by counting braces
    mobile_start = content.find('@media (max-width: 768px)')
    if mobile_start != -1:
        # Find the matching closing brace
        brace_count = 0
        start_pos = content.find('{', mobile_start)
        if start_pos != -1:
            pos = start_pos
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        mobile_content = content[mobile_start:pos+1]
                        break
                pos += 1
            else:
                mobile_content = ""
        else:
            mobile_content = ""
    else:
        mobile_content = ""

    mobile_has_correct_font = 'font-size: 1.5rem' in mobile_content
    mobile_has_correct_line_height = 'line-height: 1.8125rem' in mobile_content

    check_requirement(
        "Mobile font size is 1.5rem (24px)",
        mobile_has_correct_font
    )

    # Test 7: Mobile line height (29px = 1.8125rem)
    check_requirement(
        "Mobile line height is 1.8125rem (29px)",
        mobile_has_correct_line_height
    )

    # Test 8: Heading still exists in HTML
    check_requirement(
        "Heading 'What is AI Work Playground?' exists",
        "🚀 What is AI Work Playground?" in content
    )

    # Print summary
    print(f"\n📊 Test Summary: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All font size changes implemented correctly!")
        return True
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed. Please review the implementation.")
        return False

if __name__ == "__main__":
    success = test_font_size_changes()
    exit(0 if success else 1)
