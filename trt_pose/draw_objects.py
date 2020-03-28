from PIL import ImageDraw


class DrawObjects(object):
    def __init__(self, topology):
        self.topology = topology

    def __call__(self, image, object_counts, objects, normalized_peaks):
        draw = ImageDraw.Draw(image)
        height = image.height
        width = image.width

        K = self.topology.shape[0]
        count = int(object_counts[0])
        K = self.topology.shape[0]
        for i in range(count):
            obj = objects[0][i]
            C = obj.shape[0]

            for k in range(K):
                c_a = self.topology[k][2]
                c_b = self.topology[k][3]
                if obj[c_a] >= 0 and obj[c_b] >= 0:
                    peak0 = normalized_peaks[0][c_a][obj[c_a]]
                    peak1 = normalized_peaks[0][c_b][obj[c_b]]
                    x0 = round(float(peak0[1]) * width)
                    y0 = round(float(peak0[0]) * height)
                    x1 = round(float(peak1[1]) * width)
                    y1 = round(float(peak1[0]) * height)
                    draw.line([(x0, y0), (x1, y1)], fill=(0, 255, 0), width=2)

            for j in range(C):
                k = int(obj[j])
                if k >= 0:
                    peak = normalized_peaks[0][j][k]
                    x = round(float(peak[1]) * width)
                    y = round(float(peak[0]) * height)
                    draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(255, 0, 0))
