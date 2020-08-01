# Simple Diderot Project

This is a simple project scaffold for TAs hoping to use Diderot effectively. You need a modern version of Linux (Ubuntu/Windows Subsystem for Linux/Vagrant suggested), or possibly Mac OSX to use this.

In this course management repository, IPython notebooks are the preferred format for course hand-outs, hand-ins, and notes. I strongly recommend you use notebooks with this -- we provide these features:

- **Automatic handout packaging.**: you write a single handout including prose, empty function stubs, student-side tests, and reference implementations. From that, we:
  - Configure the autograder to only allow package imports for the Python standard library and everything in `requirements.txt` (on a per-handin basis).
  - Test your autograder and reference implementation to make sure they agree.
  - Provide students with the testing framework to check their handouts before submission. (This greatly reduces submission attempts.)
  - Package and upload the handout and autograder to Diderot Code Labs.
  - Submit the reference handin to Diderot under the TA account. (Verify that the Diderot autograder works.)
  - Generate a web page with the handout and a zipped download file. (For your course website!)
- **Notes**: write your course notes as a single IPython notebook file and this can:
  - Upload the generated notes as a chapter in a Diderot book.
  - Generate Markdown output for use in the course website.

This was originally written for the Spring 2019 run of Practical Data Science, and was later superseded by a much nicer CI-based solution (which would be overkill for smaller courses). This version is presented here, warts and all, in the hope that it can be modified to suit your needs.

## Starting

This is the developer repository that exists to import all the dependencies. To install everything, run:

```
git submodule update --init --recursive
```

When editing each homework/tools repository, you should checkout `master` before editing it. You can update all submodule tips using:

```
git submodule update --recursive --remote
```

### Repository Structure

```
.
├── homework
│   └── <homework-id>                    A directory for each homework.
│       ├── grading
│       │   └── tests.py                 Autograder tests. Required, leave empty if not needed.
│       ├── handout
│       │   ├── requirements.txt         Required, leave empty if not needed.
│       │   ├── <homework-id>_solution.ipynb      The hand-in file.
│       │   └── other-files.ext          Any other files required.
│       └── score.json                   Score breakdown for fully-correct homework. Used by `test-homework`.
├── notes
│   └── <notes-id>                       A directory for each class notes.
│       ├── <notes-id>.ipynb             Main notes file.
│       └── other-files.ext              Any other files.
├── slides
│   └── <presentation-id>                A directory for each presentation.
│       └── <presentation-id>.pdf        The presentation file. No additional files are permitted.
└── tools
    ├── autograder                       The source for the autograder Docker image.
    ├── bin                              Various compiling and upload scripts.
    ├── diderot-cli                      Provides the official Diderot CLI, used for uploading generated files.
    ├── guide                            Provides the diderot compiler dc, converts Markdown to the Diderot-native format.
    ├── nb2md                            Converts ipynb files to GitHub-flavoured Markdown and Diderot-flavoured markdown.
    └── solution2handout.py              Takes a homework master file and strips out the `##SOLUTION##` cells.
```

### More External Dependencies

In addition to the dependencies in `bin/tools`, we have these dependencies:

- Client-side tests [https://github.com/gauravmm/jupyter-testing.git](`jupyter-testing`).
- Server-side grader [https://github.com/gauravmm/autolab-testing.git](`autolab-testing`).

### Requirements

Before you can run any of these scripts, ensure that you have:

 1. Installed Docker
 2. Produced a custom docker autograder image:
   a. create a dockerhub account
   b. go to `tools/autograder` and modify `dockerhub-push.sh` with you account name
   c. run `dockerhub-push.sh` from `tools/autograder`
 3. In Diderot, create three books: `book:lecture-slides` for slides, `book:lecture-notes` for notes, and `book:homework` for homework handouts.
 4. Navigate to `tools/bin` and in each `upload-*` script, update the target course name. (This can easily be moved to a single config file -- consider doing that.)
 5. Update `TEMPLATE.diderot` with your password and move it to `.diderot`. Do not commit this file.

## Course Content

### Slides

Slides for each lecture are in `slides/<slide_id>/<slide_id>.pdf`. Feel free to add other source files in the directory, they will not be included in the course website and/or the Diderot distribution.

### Notes

Lecture or recitation notes can be included, as Jupyter Notebooks, in `notes/<lecture_id>/<lecture_id>.ipynb`. Feel free to add other source files in the directory, all these will automatically be bundled when the files are added to Diderot.

### Homework

Each homework is submitted as a single .ipynb file. The homework must be stored in `/homework/<homework_id>/handout/<homework_id>_solution.ipynb`. Feel free to add other files in the directory, all these will automatically be bundled when the files are added to Diderot.

You should include solutions as code blocks starting with `## SOLUTION ##`. Include them _after_ the problem blocks so the generated test hand-in can be used to check the autograder. These blocks are automatically stripped from the IPython notebook to generate the handout.

Include the grader as a set of files in `/homework/<homework_id>/grading/*.py`. These files are all run by the autograder.

- Run `tools/bin/build-homework <homework_id>` to build the handout, autograder, test handin, and book chapter.
- Run `tools/bin/test-homework <homework_id>` to build an autograder instance and run the test handin against the autograder on your local machine.
- Run `tools/bin/upload-homework <homework_id>` to upload the autograder and book chapter and submit the test handin.

### Generated website content

On building notes and homework, web pages are automatically generated in "*-website/" directories. This is much cheaper than generating the main Diderot files, so consider leaving it enabled even if you don't need it.

## Scripts

All scripts must be run from the root directory of the repository. Run them as `tools/bin/<script-name>`.

Here are the scripts:

- `diderot`: stub to access diderot; modify to change default arguments.
- `build-homework <homework-id> [<homework-id> ...]`: for each specified homework, build the handout, reference handin, autograder, diderot chapter, and web pages.
- `build-notes <notes-id> [<notes-id> ...]`: for each specified notes, build the diderot chapter and web pages.
- `test-homework <homework-id> [handin.tgz]`: run the autograder on the reference handin, printing the output. Requires that you have built the autograder image. You can optionally specify a student-submitted `handin.tgz` (exactly that name) to run that instead.
- `upload-homework <homework-id>`: upload the built handout, autograder, and diderot book chapter. Then submit the reference handin.
- `upload-notes <notes-id>`: upload the built diderot book chapter.
- `upload-slides <slides-id>`: upload the slides as a diderot book chapter.

## Caveats

- This builds based on your current directory structure, not on the clean commit. A simple strategy to avoid accidentally bundling side-loaded data is to:
  1. have a separate clone of this repository,
  2. pushing your changes to GitHub in the working repository,
  3. pulling these changes from your building repository,
  4. running the build and push process from there
- The course name is currently hardcoded in every script in `tools/bin/upload-*`. This should be fixed.
- Be careful when uploading book chapters. If you delete a previous book version, you will lose questions that students post.
