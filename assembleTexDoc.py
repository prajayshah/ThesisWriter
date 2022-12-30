import datetime
import os

from pylatex import Command
from pylatex.utils import NoEscape

from ThesisWriter import THESIS_DIR_TOPLEVEL, MyLtxDocument, convert_docx_to_, _open_preview

PDF_PATH = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/Thesis-ltx.pdf'


def ch_general_introduction(doc: MyLtxDocument):
    inputs = ['/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.docx',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.docx',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.docx',
              '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.docx']

    doc.add_input(*inputs)

    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex'
    # doc.add_input(tex_path=NoEscape(input_path))
    #
    # input_path = '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex'
    # doc.add_input(tex_path=NoEscape(input_path))

    return doc


def assemble_texdoc(doc: MyLtxDocument = None):
    """
    Assemble the full tex document in order with all the chapters.

    :param doc: the initialized tex doc
    """
    if doc is None:
        doc: MyLtxDocument = MyLtxDocument(
            **{'title': NoEscape('The profile of neuronal excitability in epilepsy and seizure'),
               'author': 'Prajay T. Shah',
               'date': NoEscape(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
               'filename': NoEscape('Thesis-ltx'),
               'directory': THESIS_DIR_TOPLEVEL})
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/acronyms.docx')
    doc = ch_general_introduction(doc)
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.docx')
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.docx')
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.docx')
    doc.add_input('/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.docx')
    doc.append(Command('printbibliography'))
    doc.save_ltx_tex()
    doc.save_ltx_pdf()
    _open_preview(doc.export_path + '.pdf')


# %%
# run the program using Ctrl-R in PyCharm or calling ThesisWriter.main() from the console or `python ThesisWriter.py` from the command line
if __name__ == '__main__':
    assemble_texdoc()


# _open_preview(PDF_PATH)
# convert_docx_to_(extension='.tex', directory='/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/')
# convert_docx_to_(extension='.tex', docx_files=[
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 1- Neuronal excitability.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 2- All optical technique.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Topic 3- Epilepsy and seizures.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/1_Introduction/Hypothesis.tex',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim1/aim1-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim2/aim2-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/3_Results/ch-aim3/aim3-full.docx',
#                      '/Users/prajayshah/OneDrive/UTPhD/2022/Thesis-writing/4_Discussion/Discussion_full.docx',
#                  ])