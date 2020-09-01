from Core.Module import Module
from Core.Collection import Collection

n_max_segment = 11
n_chamber = 36
n_station = 4
n_ring = 4
n_endcap = 2

class StandAloneMuonProducer(Module):
    def analyze(self,event):
        event.standAloneMuons = [m for m in Collection(event,"muons") if m.isStandAloneMuon]
        event.cscSegments = [s for s in Collection(event,"cscSegments")]
        for m in event.standAloneMuons:
            n_segment = len(m.cscSegmentRecord_endcap)
            m.segments_globalX = []
            m.segments_globalY = []
            m.segments_endcap = []
            m.segments_chamber = []
            m.segments_station = []
            m.segments_ring = []
            for i in range(n_mu_segment):
                mu_endcap = m.cscSegmentRecord_endcap[i]
                mu_chamber = m.cscSegmentRecord_chamber[i]
                mu_station = m.cscSegmentRecord_station[i]
                mu_ring = m.cscSegmentRecord_ring[i]
                mu_localX = m.cscSegmentRecord_localX[i]
                mu_localY = m.cscSegmentRecord_localY[i]
                for seg in event.cscSegments:
                    seg_endcap = seg.ID_endcap
                    seg_ring = seg.ID_ring
                    seg_station = seg.ID_station
                    seg_chamber = seg.ID_chamber
                    seg_localX = seg.localX
                    seg_localY = seg.localY
                    if seg_endcap == mu_endcap and seg_ring == mu_ring and seg_station == mu_station and seg_chamber == mu_chamber and seg_localX == mu_localX and seg_localY == mu_localY:
                        m.segments.globalX.append(seg.globalX)
                        m.segments.globalY.append(seg.globalY)
                        m.segments_endcap.append(seg_endcap)
                        m.segments_chamber.append(seg_chamber)
                        m.segments_station.append(seg_station)
                        m.segments_ring.append(seg_ring)
            
            if len(m.segments_globalX) < n_max_segment: m.segments_globalX += [0]*(n_max_segment-len(m.segments_globalX))
            if len(m.segments_globalY) < n_max_segment: m.segments_globalY += [0]*(n_max_segment-len(m.segments_globalY))
            if len(m.segments_endcap) < n_max_segment: m.segments_endcap += [0]*(n_max_segment-len(m.segments_endcap))
            if len(m.segments_chamber) < n_max_segment: m.segments_chamber += [0]*(n_max_segment-len(m.segments_chamber))
            if len(m.segments_station) < n_max_segment: m.segments_station += [0]*(n_max_segment-len(m.segments_station))
            if len(m.segments_ring) < n_max_segment: m.segments_ring += [0]*(n_max_segment-len(m.segments_ring))
        return True

    def hash(self,chamber,station,ring,endcap):
        hash_endcap = (endcap-1)*n_chamber*n_station*n_ring
        hash_chamber = (chamber-1)*n_station*n_ring
        hash_station = (station-1)*n_ring
        hash_ring = ring-1
        return hash_endcap+hash_chamber+hash_station+hash_ring+1

