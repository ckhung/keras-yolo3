#!/usr/bin/python3

import sys, argparse, json, re
from yolo import YOLO
from PIL import Image

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(
        argument_default=argparse.SUPPRESS,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    '''
    Command line options
    '''
    parser.add_argument(
        '--model_path', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors_path', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes_path', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--outdir', default='/tmp',
        help='directory where output will be stored'
    )

    parser.add_argument(
        'imgfiles', nargs='*', type=str,
        help='image file names'
    )

    FLAGS = parser.parse_args()
    yolo = YOLO(**vars(FLAGS))

    # https://stackoverflow.com/questions/1447287/format-floats-with-standard-json-module
    json.encoder.FLOAT_REPR = lambda o: format(o, '.2f')
    for fn in FLAGS.imgfiles:
        image = Image.open(fn)
        (ret, r_image) = yolo.detect_image(image)
        m = re.search(r'([^/]*)\.\w+$', fn)
        fn = FLAGS.outdir + '/' + m.group(1)
        with open(fn+'.json', 'w') as jsonfile:
            jsonfile.write((json.dumps(ret, indent=4)))
        # r_image.show()
        r_image.save(fn + '.jpg')
    yolo.close_session()

