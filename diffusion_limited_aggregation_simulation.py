import random
import math
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Constants
D = 3
DefaultParticleSpacing = 1
DefaultAttractionDistance = 3
DefaultMinMoveDistance = 1
DefaultStubbornness = 0
DefaultStickiness = 1

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.m_X = x
        self.m_Y = y
        self.m_Z = z

    def X(self):
        return self.m_X

    def Y(self):
        return self.m_Y

    def Z(self):
        return self.m_Z

    def Length(self):
        return math.sqrt(self.m_X * self.m_X + self.m_Y * self.m_Y + self.m_Z * self.m_Z)

    def LengthSquared(self):
        return self.m_X * self.m_X + self.m_Y * self.m_Y + self.m_Z * self.m_Z

    def Distance(self, v):
        dx = self.m_X - v.m_X
        dy = self.m_Y - v.m_Y
        dz = self.m_Z - v.m_Z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def Normalized(self):
        m = 1 / self.Length()
        return Vector(self.m_X * m, self.m_Y * m, self.m_Z * m)

    def __add__(self, v):
        return Vector(self.m_X + v.m_X, self.m_Y + v.m_Y, self.m_Z + v.m_Z)

    def __sub__(self, v):
        return Vector(self.m_X - v.m_X, self.m_Y - v.m_Y, self.m_Z - v.m_Z)

    def __mul__(self, a):
        return Vector(self.m_X * a, self.m_Y * a, self.m_Z * a)

    def __iadd__(self, v):
        self.m_X += v.m_X
        self.m_Y += v.m_Y
        self.m_Z += v.m_Z
        return self


def Lerp(a, b, d):
    return a + (b - a).Normalized() * d

def Random(lo=0, hi=1):
    return random.uniform(lo, hi)

def RandomInUnitSphere():
    while True:
        p = Vector(Random(-1, 1), Random(-1, 1), 0 if D == 2 else Random(-1, 1))
        if p.LengthSquared() < 1:
            return p

class Model:
    def __init__(self):
        self.m_ParticleSpacing = DefaultParticleSpacing
        self.m_AttractionDistance = DefaultAttractionDistance
        self.m_MinMoveDistance = DefaultMinMoveDistance
        self.m_Stubbornness = DefaultStubbornness
        self.m_Stickiness = DefaultStickiness
        self.m_BoundingRadius = 0
        self.m_Points = []
        self.m_JoinAttempts = []

    def Add(self, p, parent=-1):
        id_ = len(self.m_Points)
        self.m_Points.append(p)
        self.m_JoinAttempts.append(0)
        self.m_BoundingRadius = max(self.m_BoundingRadius, p.Length() + self.m_AttractionDistance)
        print(f"{id_},{parent},{p.X()},{p.Y()},{p.Z()}")

    def Nearest(self, point):
        distances = [point.Distance(p) for p in self.m_Points]
        return distances.index(min(distances))

    def RandomStartingPosition(self):
        d = self.m_BoundingRadius
        return RandomInUnitSphere().Normalized() * d

    def ShouldReset(self, p):
        return p.Length() > self.m_BoundingRadius * 2

    def ShouldJoin(self, p, parent):
        self.m_JoinAttempts[parent] += 1
        if self.m_JoinAttempts[parent] < self.m_Stubbornness:
            return False
        return Random() <= self.m_Stickiness

    def PlaceParticle(self, p, parent):
        return Lerp(self.m_Points[parent], p, self.m_ParticleSpacing)

    def MotionVector(self, p):
        return RandomInUnitSphere()

    def AddParticle(self):
        p = self.RandomStartingPosition()
        while True:
            parent = self.Nearest(p)
            d = p.Distance(self.m_Points[parent])

            if d < self.m_AttractionDistance:
                if not self.ShouldJoin(p, parent):
                    p = Lerp(self.m_Points[parent], p, self.m_AttractionDistance + self.m_MinMoveDistance)
                    continue
                p = self.PlaceParticle(p, parent)
                self.Add(p, parent)
                return

            m = max(self.m_MinMoveDistance, d - self.m_AttractionDistance)
            p += self.MotionVector(p).Normalized() * m

            if self.ShouldReset(p):
                p = self.RandomStartingPosition()


def visualize_particles_matplotlib(points, D=2):
    if D == 2:
        x = [point.m_X for point in points]
        y = [point.m_Y for point in points]

        plt.scatter(x, y, s=3, c='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('2D Particle Distribution')
        plt.grid(True)
        plt.show()
    elif D == 3:
        x = [point.m_X for point in points]
        y = [point.m_Y for point in points]
        z = [point.m_Z for point in points]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, s=3, c='blue')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Particle Distribution')
        plt.show()


# Visualization
def visualize_particles_plotly(points, D=2, marker_size=5):
    num_points = len(points)
    colors = list(range(num_points))  # Assigning a unique color index based on the age

    if D == 2:
        x = [point.m_X for point in points]
        y = [point.m_Y for point in points]

        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers',
                                        marker=dict(size=marker_size, color=colors, colorscale='Phase', opacity=0.6)))
        fig.update_layout(title='2D Particle Distribution',
                          xaxis_title='X',
                          yaxis_title='Y')
        fig.show()

    elif D == 3:
        x = [point.m_X for point in points]
        y = [point.m_Y for point in points]
        z = [point.m_Z for point in points]

        fig = go.Figure(data=go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                          marker=dict(size=marker_size, color=colors, colorscale='Plotly3', opacity=0.6)))
        fig.update_layout(title='3D Particle Distribution',
                          scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
        fig.show()

        # Save to HTML
        fig.write_html("DLA_visualization.html")


if __name__ == "__main__":
    model = Model()
    model.Add(Vector())

    for i in range(10000):
        model.AddParticle()

    # visualize_particles_matplotlib(model.m_Points, D)
    visualize_particles_plotly(model.m_Points, D)

