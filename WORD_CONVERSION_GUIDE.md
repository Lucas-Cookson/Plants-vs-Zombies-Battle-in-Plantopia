# Instructions for Converting Documentation to Word Format

## Converting DOCUMENTATION.md to Word Document

The comprehensive project documentation is provided in DOCUMENTATION.md. To convert it to a Microsoft Word document (.docx) as required by the assignment:

### Option 1: Using Microsoft Word (Recommended)

1. Open Microsoft Word
2. Create a new blank document
3. Go to File → Open and select DOCUMENTATION.md
4. Word will convert the markdown format to a Word document
5. The document will have:
   - Proper heading hierarchy (Heading 1, 2, 3 styles)
   - Numbered sections and page numbers
   - Professional formatting
6. Save as "Phase_2_Documentation.docx"

### Option 2: Using Google Docs

1. Go to Google Drive
2. Click "New" → "Google Docs"
3. Go to File → Open
4. Upload DOCUMENTATION.md
5. Google Docs will convert the content
6. Download as Word document (.docx)

### Option 3: Using Pandoc (Command Line)

If you have Pandoc installed:
```bash
pandoc DOCUMENTATION.md -o Phase_2_Documentation.docx
```

### Adding Page Numbers and Cover Design

After opening the document in Word:

1. **Insert Page Numbers:**
   - Go to Insert → Page Numbers
   - Choose position and format
   - Ensure "Different first page" is checked for title page

2. **Title Page Formatting:**
   - Title Page should be Page 1 (no page number visible)
   - Use large font (28pt) for the title
   - Center all text on title page
   - Add a page break after title page

3. **Table of Contents:**
   - Position cursor after title page break
   - Go to References → Table of Contents
   - Select a style
   - Word will auto-generate from your headings

4. **Document Sections:**
   - Each main section (Requirements, Design, etc.) should start with a page break
   - Apply Heading 1 style to main sections
   - Apply Heading 2 style to subsections

## Document Structure in the Provided Markdown

The DOCUMENTATION.md file contains:

- **Title Page**: Complete title information with team names, date, class
- **Table of Contents**: Manual listing (auto-generate in Word)
- **Requirements** (Pages 3-4):
  - Project Purpose
  - Game Requirements
  - Plant Types (Sunflower, Walnut)
  - Zombie Types (Regular, Fast)
  - Implemented Interactions
  - Graphics Requirements

- **Design** (Pages 5-8):
  - Architecture Overview (MVC pattern)
  - Class Design with code structure
  - Game Loop Flow
  - Collision Detection Algorithm
  - Level Progression Logic
  - MVC Implementation Details

- **Lessons Learned** (Page 9):
  - 10 key lessons from Phase 2 development

- **References** (Page 10):
  - IEEE-format citations of all sources used

- **GitHub Repository Overview** (Page 11):
  - Repository management practices
  - Commit strategy
  - Collaboration workflow

- **Test Coverage Summary** (Page 12):
  - Test files and coverage details
  - Test statistics
  - Verification details

## Customization Notes

Before finalizing the Word document, update the following placeholders:

1. **Team Members:** Replace "[Your Names Here]" with actual team member names
2. **Class Name:** Replace "[Class Name]" with the actual class name
3. **GitHub URL:** Replace "[INSERT GITHUB REPOSITORY URL HERE]" with actual repository URL

## Final Checklist

Before submitting the .docx file:

- [ ] Title page formatted with all team member names
- [ ] Page numbers visible on all pages except title page
- [ ] Table of contents auto-generated and links work
- [ ] All sections have proper heading hierarchy
- [ ] Class name and date filled in
- [ ] GitHub repository URL updated in two locations
- [ ] Pseudocode is clearly formatted
- [ ] All figures/diagrams embedded
- [ ] References formatted in IEEE style
- [ ] File saved as .docx (not .doc or .pdf)

## File Naming

Save the final Word document as:
```
Phase_2_Documentation.docx
```

This will be included in the final submission zip file along with:
- All Python source files (.py)
- requirements.txt
- README.md
- tests/ directory
- DOCUMENTATION.md (markdown backup)
- .git repository history
