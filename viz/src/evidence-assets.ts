import profilePhoto from '../public/photo.jpg'
import ibmPatent from '../../data/evidence/images/awards/ibm-first-patent-invention-achievement-2010.png'
import ibmInfluence from '../../data/evidence/images/awards/ibm-rtle-2010-most-influential-tec-india.png'
import serviceMaterials from '../../data/evidence/images/social-giving-back/slide-27.jpg'
import type { PortfolioSource } from './portfolio-types'

export { profilePhoto }

interface DocumentaryAssetDefinition {
  id: string
  url: string
  alt: string
  sourcePattern: RegExp
  routes: string[]
}

export interface DocumentaryAsset extends DocumentaryAssetDefinition {
  source: PortfolioSource
}

const documentaryAssetDefinitions: DocumentaryAssetDefinition[] = [
  {
    id: 'ibm-patent',
    url: ibmPatent,
    alt: 'IBM invention achievement certificate',
    sourcePattern: /patent|invention achievement/i,
    routes: ['brief', 'innovation', 'data'],
  },
  {
    id: 'ibm-influence',
    url: ibmInfluence,
    alt: 'IBM technical community recognition certificate',
    sourcePattern: /most influential|rtle|technical community/i,
    routes: ['leadership', 'trust', 'data'],
  },
  {
    id: 'service-materials',
    url: serviceMaterials,
    alt: 'Stacks of notebooks prepared for educational distribution',
    sourcePattern: /book.*distribution|rural.*education|social.*giving|community.*service/i,
    routes: ['community', 'service', 'data'],
  },
]

export function documentaryAssetsForSources(
  sources: PortfolioSource[],
  route = '',
): DocumentaryAsset[] {
  const usedSources = new Set<string>()
  return documentaryAssetDefinitions.flatMap(definition => {
    if (route && !definition.routes.some(token => route.includes(token))) return []
    const source = sources.find(candidate =>
      !usedSources.has(candidate.id) && definition.sourcePattern.test(candidate.title)
    )
    if (!source) return []
    usedSources.add(source.id)
    return [{ ...definition, source }]
  })
}

export function documentaryAssetForSource(source: PortfolioSource): DocumentaryAsset | undefined {
  const definition = documentaryAssetDefinitions.find(item => item.sourcePattern.test(source.title))
  return definition ? { ...definition, source } : undefined
}
